REPO := registry.poc.ein.plus/dummy
TAG := $(shell legacy_lain meta)
PORT := 5000

.PHONY: build
build:
	docker build --squash -t $(REPO):release-$(TAG) .

.PHONY: push
push:
	docker push $(REPO):$(TAG)

.PHONY: run
run:
	# docker run -it --publish $(PORT):$(PORT) --rm $(REPO):release-$(TAG) ./run.py --port $(PORT)
	docker run -it --publish $(PORT):$(PORT) --rm $(REPO):release-$(TAG) bash
