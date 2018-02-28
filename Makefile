PYTHON=$(shell which python)

LINT_FILES = $(wildcard iocontrol/*.py)

LINT_FILES := $(filter-out iocontrol/pyqt_style_rc.py \
		iocontrol/pyqt5_style_rc.py, \
		$(LINT_FILES))

.PHONY: clean wheel source pylint

all: wheel

pylint:
	pylint --reports=n $(LINT_FILES)

source:
	$(PYTHON) setup.py sdist

wheel: source
	$(PYTHON) setup.py bdist_wheel

clean:
	rm -f *.pyc iocontrol/*.pyc
	rm -rf dist build iocontrol.egg-info
