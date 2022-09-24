SHELL := /bin/bash

all: install-dev

install:
	python -m pip install --upgrade .

install-dev:
	python -m venv venv # Create virtual environment
	source venv/bin/activate # Activate virtual environment
	python -m pip install --editable . # Install the package in dev mode

activate:
	source venv/bin/activate # Activate virtual environment

test:
	pytest arithmetic_solver/tests -v
