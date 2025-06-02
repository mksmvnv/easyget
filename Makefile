.PHONY: all lint build run stop logs clean rebuild

WORK_DIR	?= core
IMAGE_NAME 	?= easyget

all: lint build run

lint:
	@black ./$(WORK_DIR)

build:
	@docker build -t $(IMAGE_NAME) .

run:
	@docker run -d --name $(IMAGE_NAME) \
	--restart unless-stopped $(IMAGE_NAME)

stop:
	@docker stop $(IMAGE_NAME)

logs:
	@docker logs -f $(IMAGE_NAME)

clean:
	@docker rm -f $(IMAGE_NAME)
	@docker rmi $(IMAGE_NAME)

rebuild: stop clean all
