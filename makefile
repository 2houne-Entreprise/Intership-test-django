.PHONY: run migrate  

PYTHON := .venv/Scripts/python.exe

run:
	$(PYTHON) manage.py runserver

migrate:
	$(PYTHON) manage.py migrate
