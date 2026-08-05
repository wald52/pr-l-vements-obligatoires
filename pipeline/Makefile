# Pipeline d'inventaire des prélèvements obligatoires.
# Usage : make install && make all   (ou make offline pour le cache local)

PY ?= python
export PYTHONPATH := src

.PHONY: install all offline fetch normalize classify reconcile report workdoc validate test clean

install:
	$(PY) -m pip install -r requirements.txt

all:
	$(PY) -m po_pipeline all

offline:
	$(PY) -m po_pipeline all --offline

fetch:
	$(PY) -m po_pipeline fetch

normalize:
	$(PY) -m po_pipeline normalize

classify:
	$(PY) -m po_pipeline classify

reconcile:
	$(PY) -m po_pipeline reconcile

validate:
	$(PY) -m po_pipeline validate

report:
	$(PY) -m po_pipeline report

workdoc:
	$(PY) -m po_pipeline workdoc

test:
	$(PY) -m pytest -q

clean:
	rm -rf data/raw/* data/interim/* data/processed/*
