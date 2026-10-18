

.PHONY: run migrate makemigrations test

PYTHON := .venv/Scripts/python.exe

run:
	$(PYTHON) manage.py runserver

migrate:
	$(PYTHON) manage.py migrate

makemigrations:
	$(PYTHON) manage.py makemigrations

test:
	$(PYTHON) manage.py test