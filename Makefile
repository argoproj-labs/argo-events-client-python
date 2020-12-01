ARGO_EVENTS_VERSION := v1.1.0

CLIENT_VERSION := v0.1.0

GENERATOR_VERSION := v4.3.1

PACKAGE_NAME := argo.events.client

ARGO_EVENTS_SPEC := ./openapi/spec/events-${ARGO_EVENTS_VERSION}-swagger.json

OPENAPI_SPEC = ./openapi/swagger.json

OUTPUT_DIR = ./gen

.PHONY: all
all: clean fetch preprocess gen patch

.PHONY: clean
clean:
	rm -rf gen
	mkdir gen

.PHONY: fetch
fetch:
	rm -Rf ./docs ./src/test ./openapi
	mkdir -p ./openapi/spec
	curl -L -o ${ARGO_EVENTS_SPEC} https://raw.githubusercontent.com/argoproj/argo-events/$(ARGO_EVENTS_VERSION)/api/openapi-spec/swagger.json

.PHONY: preprocess
preprocess:
	python3 ./scripts/preprocess.py -i ${ARGO_EVENTS_SPEC} \
 -d 'io.argoproj.eventbus.v1alpha1' \
 -d 'io.argoproj.eventsource.v1alpha1' \
 -d 'io.argoproj.common' \
 -d 'io.argoproj.sensor.v1alpha1' \
 -d 'io.k8s.api.core' \
-d 'io.k8s.apimachinery.pkg.apis.meta' \
-o ${OPENAPI_SPEC}

.PHONY: gen
gen:
	@echo "Generating Argo Events ${CLIENT_VERSION} client"
	docker run --rm -v $(shell pwd):/local openapitools/openapi-generator-cli:v4.3.1 generate \
		-g python \
		-i /local/${OPENAPI_SPEC} \
		-o /local/${OUTPUT_DIR} \
		--global-property modelTests=false \
    --global-property projectName=argo-events-client \
		--additional-properties=packageUrl=https://github.com/argoproj-labs/argo-events-client-python \
		--additional-properties=packageVersion=${CLIENT_VERSION} \
		--additional-properties=packageName=${PACKAGE_NAME}

.PHONY: patch
patch:
	@echo "--- Patching generated code..."
  # Fix imports
	find "${OUTPUT_DIR}/argo/events/" -type f -name \*.py -exec sed -i 's/import openapi_client\./import argo.events.client./g' {} +
	find "${OUTPUT_DIR}/argo/events/" -type f -name \*.py -exec sed -i 's/from openapi_client/from argo.events.client/g' {} +
	find "${OUTPUT_DIR}/argo/events/" -type f -name \*.py -exec sed -i 's/getattr(openapi_client\.models/getattr(argo.events.client.models/g' {} +
	find "${OUTPUT_DIR}/argo/events/" -type f -name \*_v1_container.py -exec sed -i 's/name\=None/name\=\'\''/g' {} +

	@echo "Replace io.k8s models with python kubernetes.client.library"
	find "${OUTPUT_DIR}/argo/events/" -type f \
        -exec sed -i "/import IoK8s/d" {} \; \
        -exec sed -i "s/IoK8sApiCore\|IoK8sApimachineryPkgApisMeta//g" {} \;

	cp ./scripts/__about__.py ${OUTPUT_DIR}/argo/events/client/__about__.py
	cp ./scripts/setup.py ${OUTPUT_DIR}
	sed -i "s/__version__ = \(.*\)/__version__ = \"${CLIENT_VERSION}\"/g" ${OUTPUT_DIR}/argo/events/client/__about__.py

builder_make:
	docker run -w `pwd` -it --entrypoint make --rm -v `pwd`:`pwd` -v /var/run/docker.sock:/var/run/docker.sock ${BUILDER_IMAGE}
