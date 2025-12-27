.PHONY: help install validate clean

PYTHON ?= python3
PIP ?= pip3

SCHEMA := decision-log/decision-log.schema.json
EXAMPLE := examples/rgds-dec-0001.json
VALIDATOR := scripts/validate_decision_log.py

help:
	@echo "RGDS – Regulated Gate Decision Support"
	@echo ""
	@echo "Available commands:"
	@echo "  make install   Install Python dependencies"
	@echo "  make validate  Validate example decision log against schema"
	@echo "  make clean     Remove Python cache files"

install:
	$(PIP) install -r requirements.txt

validate:
	$(PYTHON) $(VALIDATOR) $(SCHEMA) $(EXAMPLE)

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
