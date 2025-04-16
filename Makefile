WORKDIR=./core

all: lint run

lint:
	black $(WORKDIR)

run:
	python3 $(WORKDIR)/app.py
