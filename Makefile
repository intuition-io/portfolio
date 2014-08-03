# Makefile
# vim:ft=make

LOGS?=/tmp/make-portfolio.logs

all: dependencies install

install:
	python setup.py install

dependencies:
	@echo "[make] Installing packages"
	sudo apt-get update -y
	sudo apt-get -y --no-install-recommends install libopenblas-dev liblapack-dev gfortran 2>&1 >> ${LOGS}
	@echo "[make] Installing python modules"
	pip install --quiet --use-mirrors distribute 2>&1 >> ${LOGS}
	pip install --quiet --use-mirrors numpy 2>&1 >> ${LOGS}

package:
	# NOTE Replace the version in portfolio.__init__.py ?
	@echo "[make] Committing changes"
	git add -A
	git commit
	git tag ${VERSION}
	git push --tags
	@echo "[make] Packaging portfolio"
	python setup.py sdist
	python setup.py sdist upload

tests: warn_missing_linters
	# TODO Recursively analyze all files and fail on conditions
	@echo -e '\tChecking complexity (experimental) ...'
	radon cc -ana portfolio/analytics.py
	@echo -e '\tChecking requirements ...'
	# TODO Fail if outdated
	piprot --outdated requirements.txt dev-requirements.txt
	@echo -e '\tChecking syntax ...'
	pep8 --exclude _review --ignore E265 tests portfolio
	@echo -e '\tRunning tests ...'
	nosetests -s -w tests --with-yanc --with-coverage --cover-package=portfolio

present_pep8=$(shell which pep8)
present_radon=$(shell which radon)
present_nose=$(shell which nosetests)
present_piprot=$(shell which piprot)
warn_missing_linters:
	@test -n "$(present_radon)" || echo "WARNING: radon not installed."
	@test -n "$(present_pep8)" || echo "WARNING: pep8 not installed."
	@test -n "$(present_nose)" || echo "WARNING: nose not installed."
	@test -n "$(present_piprot)" || echo "WARNING: piprot not installed."

.PHONY: dependencies install warn_missing_linters tests package
