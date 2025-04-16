WORKDIR=./

all: lint run

lint:
	black $(WORKDIR)

run:
	python3 app.py
