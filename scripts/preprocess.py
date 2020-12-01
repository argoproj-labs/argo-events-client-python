# Copyright 2016 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function

import argparse
import json
import operator
import os.path
import re
import sys
import urllib3

from collections import OrderedDict

_ops = ["get", "put", "post", "delete", "options", "head", "patch", "watch"]


class PreprocessingException(Exception):
    pass


def _title(s):
    if len(s) == 0:
        return s
    return s[0].upper() + s[1:]


def _to_camel_case(s):
    return "".join(_title(y) for y in s.split("_"))


def _has_property(prop_list, property_name):
    for prop in prop_list:
        if prop["name"] == property_name:
            return True


def process_swagger(spec_path):
    with open(spec_path, "r") as f:
        spec = json.loads(f.read())

    apply_func_to_spec_operations(spec, strip_tags_from_operation_id)
    apply_func_to_spec_operations(spec, add_codegen_request_body)

    operation_ids = {}
    apply_func_to_spec_operations(
        spec, lambda op, _: operator.setitem(operation_ids, op["operationId"], op)
    )

    inline_primitive_models(spec, [])

    return spec


def apply_func_to_spec_operations(spec, func, *params):
    """Apply func to each operation in the spec.

    :param spec: The OpenAPI spec to apply func to.
    :param func: the function to apply to the spec's operations. It should be
                 a func(operation, parent) where operation will be each
                 operation of the spec and parent would be the parent object of
                 the given operation.
                 If the return value of the func is True, then the operation
                 will be deleted from the spec.
    """
    for k, v in spec["paths"].items():
        for op in _ops:
            if op not in v:
                continue
            if func(v[op], v, *params):
                del v[op]


def strip_tags_from_operation_id(operation, _):
    operation_id = operation["operationId"]
    if "tags" in operation:
        for t in operation["tags"]:
            operation_id = operation_id.replace(_to_camel_case(t), "")
        operation["operationId"] = operation_id


def add_codegen_request_body(operation, _):
    if "parameters" in operation and len(operation["parameters"]) > 0:
        if operation["parameters"][0].get("in") == "body":
            operation["x-codegen-request-body-name"] = "body"


def inline_primitive_models(spec, excluded_primitives):
    to_remove_models = []
    for k, v in spec['definitions'].items():
        if k in excluded_primitives:
            continue
        if "properties" not in v:
            if k == "intstr.IntOrString":
                v["type"] = "object"
            if "type" not in v:
                v["type"] = "object"
            print("Making model `%s` inline as %s..." % (k, v["type"]))
            find_replace_ref_recursive(spec, "#/definitions/" + k, v)
            to_remove_models.append(k)

    for k in to_remove_models:
        del spec['definitions'][k]

def find_rename_ref_recursive(root, old, new):
    if isinstance(root, list):
        for r in root:
            find_rename_ref_recursive(r, old, new)
    if isinstance(root, dict):
        if "$ref" in root:
            if root["$ref"] == old:
                root["$ref"] = new
        for k, v in root.items():
            find_rename_ref_recursive(v, old, new)


def remove_model_prefixes(spec, prefixes):
    """Remove full package name from OpenAPI model names.

    Starting kubernetes 1.6, all models has full package name. This is
    verbose and inconvenient in python client. This function tries to remove
    parts of the package name but will make sure there is no conflicting model
    names. This will keep most of the model names generated by previous client
    but will change some of them.
    """
    prefixes = prefixes or []

    remove_deprecated_models(spec)

    models = {}
    for k, v in spec["definitions"].items():
        if any(k.startswith(p) for p in prefixes):
            models[k] = {"split_n": 2}

    conflict = True
    while conflict:
        for k, v in models.items():
            splits = k.rsplit(".", v["split_n"])
            v["removed_prefix"] = splits.pop(0)
            v["new_name"] = ".".join(splits)

        conflict = False
        for k, v in models.items():
            for k2, v2 in models.items():
                if k != k2 and v["new_name"] == v2["new_name"]:
                    v["conflict"] = True
                    v2["conflict"] = True
                    conflict = True

        if conflict:
            for k, v in models.items():
                if "conflict" in v:
                    print("Resolving conflict for %s" % k)
                    v["split_n"] += 1
                    del v["conflict"]

    for k, v in models.items():
        if "new_name" not in v:
            raise PreprocessingException("Cannot rename model %s" % k)
        rename_model(spec, k, v["new_name"])

    return spec


def rename_model(spec, old_name, new_name):
    if new_name in spec["definitions"]:
        raise PreprocessingException(
            "Cannot rename model %s. new name %s exists." % (old_name, new_name)
        )

    find_rename_ref_recursive(
        spec, "#/definitions/" + old_name, "#/definitions/" + new_name
    )

    spec["definitions"][new_name] = spec["definitions"][old_name]

    del spec["definitions"][old_name]


def remove_deprecated_models(spec):
    """
    In kubernetes 1.8 some of the models are renamed. Our remove_model_prefixes
    still creates the same model names but there are some models added to
    reference old model names to new names. These models broke remove_model_prefixes
    and need to be removed.
    """
    models = {}
    for k, v in spec["definitions"].items():
        if is_model_deprecated(v):
            print("Removing deprecated model %s" % k)
        else:
            models[k] = v
    spec["definitions"] = models


def is_model_deprecated(m):
    """
    Check if a mode is deprecated model redirection.

    A deprecated mode redirecation has only two members with a
    description starts with "Deprecated." string.
    """
    if len(m) != 2:
        return False
    if "$ref" not in m or "description" not in m:
        return False
    return m["description"].startswith("Deprecated.")


def find_replace_ref_recursive(root, ref_name, replace_map):
    if isinstance(root, list):
        for r in root:
            find_replace_ref_recursive(r, ref_name, replace_map)
    if isinstance(root, dict):
        if "$ref" in root:
            if root["$ref"] == ref_name:
                del root["$ref"]
                for k, v in replace_map.items():
                    if k in root:
                        if k != "description":
                            raise PreprocessingException(
                                "Cannot inline model %s because of "
                                "conflicting key %s." % (ref_name, k)
                            )
                        continue
                    root[k] = v
        for k, v in root.items():
            find_replace_ref_recursive(v, ref_name, replace_map)


def write_json(fp, obj):
    dump = lambda obj, out: json.dump(
        obj, out, sort_keys=False, indent=2, separators=(",", ": "), ensure_ascii=True
    )
    if isinstance(fp, str):
        with open(fp, "w") as out:
            dump(obj, out)
        return

    dump(obj, fp)


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        "-i", "--input-file", required=True, help="Path to the input OpenAPI spec"
    )
    argparser.add_argument(
        "-o",
        "--output-file",
        default=sys.stdout,
        help="Path to the output OpenAPI spec",
    )
    argparser.add_argument(
        "-d",
        "--strip",
        action="append",
        dest="to_strip",
        nargs="?",
        help="Prefixes to be stripped from the models.",
    )
    args = argparser.parse_args()

    spec = process_swagger(args.input_file)
    spec = remove_model_prefixes(spec, args.to_strip)

    write_json(args.output_file, spec)
    sys.exit(0)


if __name__ == "__main__":
    sys.exit(main())
