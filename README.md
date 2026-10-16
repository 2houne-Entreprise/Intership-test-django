# Internship Test — Django

Toutes les instructions et consignes relatives à ce projet sont décrites dans le fichier [ISSUE.md](./ISSUE.md) de ce dépôt.

Veuillez lire l'issue en entier avant de commencer.

## 🧱 Contenu du dépôt

Ce dépôt ne contient **volontairement aucun code** :

* `ISSUE.md` — le sujet du test technique (US1 à US8) ;
* `.github/workflows/django-tests.yml` — le workflow d'intégration continue, qui exécute `python manage.py check` puis `python manage.py test` une fois le projet créé ;
* `.gitignore` — les fichiers Python / Django à ne pas versionner.

L'initialisation du projet Django (US1) fait partie du test : à vous de la réaliser.

## 🚀 Démarrage

```bash
# 1. Créer le projet (US1)
python -m venv .venv
source .venv/bin/activate        # Windows : .venv\Scripts\activate
pip install "Django~=6.1.0"
django-admin startproject config .

# 2. Créer le reste de l'application, puis :
pip freeze > requirements.txt
python manage.py migrate
python manage.py runserver       # http://127.0.0.1:8000
python manage.py test
```

## Workflow

Pour contribuer à la résolution de l'issue, créez une nouvelle branche nommée `feature/<nom-stagiaire>` à partir de `develop`, résolvez l'issue, puis ouvrez une pull request vers `develop`.
