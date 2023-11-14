install:
	@echo "Installing..."
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	python -m textblob.download_corpora
	@echo "Install Complete"

test:
	@echo "Running tests..."
	python -m pytest -vv --cov=nlp_lib.app tests/test_app.py
	@echo "Tests Complete"

format:
	@echo "Formatting..."
	find . -type f -name '*.py' | xargs black
	@echo "Format Complete"

lint:
	@echo "Linting..."
	find . -type f -name '*.py' | xargs pylint --disable=R,C
	@echo "Lint Complete"

all: install test format lint