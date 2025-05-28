WORKDIR=./core
IMAGE=easyget

all: lint build run

lint:
	black $(WORKDIR)
build:
	docker build -t $(IMAGE) .
run:
	docker run --rm -d --name $(IMAGE) $(IMAGE)
stop:
	docker stop $(IMAGE)
logs:
	docker logs -f $(IMAGE)

.PHONY: build run stop logs
