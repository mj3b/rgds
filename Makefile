.PHONY: help install validate validate-all validate-semantic validate-strict clean

PYTHON ?= python3
PIP ?= pip3

SCHEMA := decision-log/decision-log.schema.json
EXAMPLE := examples/rgds-dec-0001.json

VALIDATE_ONE := scripts/validate_decision_log.py
VALIDATE_ALL := scripts/validate_all_examples.py

help:
	@echo "RGDS – Regulated Gate Decision Support"
	@echo ""
	@echo "Available commands:"
	@echo "  make install            Install Python dependencies"
	@echo "  make validate           Validate the default example (schema-only)"
	@echo "  make validate-semantic  Validate the default example (schema + semantic)"
	@echo "  make validate-strict    Validate the default example (semantic warnings fail)"
	@echo "  make validate-all       Validate all examples (schema + semantic + warnings)"
	@echo "  make clean              Remove Python cache files"

install:
	$(PIP) install -r requirements.txt

validate:
	$(PYTHON) $(VALIDATE_ONE) $(SCHEMA) $(EXAMPLE)

validate-semantic:
	$(PYTHON) $(VALIDATE_ONE) $(SCHEMA) $(EXAMPLE) --semantic

validate-strict:
	$(PYTHON) $(VALIDATE_ONE) $(SCHEMA) $(EXAMPLE) --strict

validate-all:
	$(PYTHON) $(VALIDATE_ALL)

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
