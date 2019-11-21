REPO := registry.poc.ein.plus/dummy
TAG := $(shell legacy_lain meta)
PORT := 5000

.PHONY: build
build:
	lain build

.PHONY: push
push:
	lain use bei
	lain push
	docker tag $(REPO):release-$(TAG) $(REPO):latest
	docker push $(REPO):latest

.PHONY: run
run:
	# docker run -it --publish $(PORT):$(PORT) --rm $(REPO):release-$(TAG) ./run.py --port $(PORT)
	docker run -it --publish $(PORT):$(PORT) --rm $(REPO):release-$(TAG) bash
