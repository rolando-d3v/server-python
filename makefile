run:
    fastapi dev src/main.py --port 4000


venv:
	python -m venv venv


install:
	pip install -r requirements.txt

