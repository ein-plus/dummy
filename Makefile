REPO := ccr.ccs.tencentyun.com/ein-lain/dummy
TAG := $(shell date +%Y%m%d)
PORT := 5000

.PHONY: build
build:
	docker build --squash -t $(REPO):$(TAG) .

.PHONY: push
push:
	docker push $(REPO):$(TAG)

.PHONY: run
run:
	docker run -it --publish $(PORT):$(PORT) --rm $(REPO):$(TAG) ./run.py --port $(PORT)
