# TaskFlow — Application de gestion de projets et de tâches

TaskFlow est une application web développée avec Django. Elle permet aux utilisateurs de gérer leurs projets et les tâches associées, de suivre leur état d'avancement et d'ajouter des pièces jointes aux tâches.

Le projet a été réalisé dans le cadre d'un test technique de stage. Les fonctionnalités développées correspondent aux User Stories (US1 à US8) décrites dans le fichier [ISSUE.md](./ISSUE.md).

## Fonctionnalités principales

- Authentification et protection des pages.
- Création, consultation, modification et suppression des projets.
- Gestion des tâches associées aux projets.
- Suivi du statut des tâches : en attente, en cours et terminée.
- Gestion des échéances et identification des tâches en retard.
- Ajout de pièces jointes aux tâches.
- Vérification des permissions pour protéger les projets des utilisateurs.
- Tests automatisés avec `Django TestCase`.

## Technologies utilisées

- **Python** : langage de programmation.
- **Django 6.1** : framework web utilisé pour développer l'application.
- **SQLite** : base de données utilisée en développement.
- **HTML** : création des interfaces utilisateur.
- **Git et GitHub** : gestion des versions et collaboration.
- **Makefile** : simplification des commandes courantes du projet.
- **Django TestCase** : tests unitaires et fonctionnels.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé :

- Python compatible avec Django 6.1.
- `pip`, pour installer les dépendances Python.
- Git, pour récupérer le dépôt.
- GNU Make, si vous souhaitez utiliser les commandes du `Makefile`.

## Installation et démarrage

### 1. Récupérer le projet

Clonez le dépôt, puis placez-vous dans son dossier :

```bash
git clone https://github.com/2houne-Entreprise/Intership-test-django.git
cd Intership-test-django
```


### 2. Créer un environnement virtuel

```bash
python -m venv .venv
```

L'environnement virtuel permet d'isoler les dépendances du projet des autres installations Python.

### 3. Activer l'environnement virtuel

**Windows — PowerShell :**

```powershell
.\.venv\Scripts\Activate.ps1
```

Si PowerShell bloque l'activation du script, vous pouvez utiliser directement l'interpréteur de l'environnement virtuel sans l'activer.

**Linux / macOS :**

```bash
source .venv/bin/activate
```

### 4. Installer les dépendances


```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Si le fichier n'existe pas encore, installez la version de Django compatible avec le projet, puis générez le fichier des dépendances :

```bash
python -m pip install "Django~=6.1.0"
python -m pip freeze > requirements.txt
```


### 5. Appliquer les migrations

```bash
python manage.py migrate
```

Cette commande crée ou met à jour les tables de la base de données selon les migrations disponibles.

Pour générer de nouvelles migrations après une modification des modèles :

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Vérifier le projet

```bash
python manage.py check
```

Cette commande vérifie la configuration du projet et signale les problèmes détectés par Django.

### 7. Lancer le serveur de développement

```bash
python manage.py runserver
```

L'application est accessible à l'adresse suivante :

http://127.0.0.1:8000/

Pour arrêter le serveur, utilisez `Ctrl + C` dans le terminal.

## Utilisation du Makefile

Le projet dispose d'un `Makefile` qui simplifie l'exécution des commandes les plus fréquentes.

Dans ce projet, les commandes utilisent l'interpréteur situé dans `.venv/Scripts/python.exe`, ce qui est adapté à Windows.

| Commande | Description |
|---|---|
| `make run` | Lance le serveur de développement. |
| `make makemigrations` | Génère les migrations correspondant aux changements des modèles. |
| `make migrate` | Applique les migrations à la base de données. |
| `make test` | Exécute les tests automatisés du projet. |

### Exemple de workflow quotidien

Après avoir modifié un modèle :

```bash
make makemigrations
make migrate
make test
make run
```

**Remarque :** ces commandes supposent que GNU Make est installé et que le `Makefile` contient bien les cibles indiquées. Si Make n'est pas disponible, utilisez les commandes `python manage.py` présentées dans la section précédente.

Pour exécuter les tests d'une application précise, vous pouvez utiliser directement Django :

```bash
python manage.py test projects
python manage.py test TaskManager
python manage.py test TaskFlow
```

La commande `make test` exécute les tests selon la cible définie dans le `Makefile`.

## Base de données et fichiers

### Base de données

Le projet utilise SQLite en environnement de développement. Sa configuration se trouve dans `config/settings.py` :

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

Le fichier `db.sqlite3` est créé automatiquement lorsque les migrations sont appliquées.

### Pièces jointes

Les fichiers ajoutés aux tâches sont gérés par le système de stockage de fichiers de Django. En développement, la configuration utilise les paramètres `MEDIA_URL` et `MEDIA_ROOT` dans `config/settings.py`.

Les pièces jointes sont stockées dans le sous-dossier `attachments/` du répertoire des médias.

Les fichiers utilisateurs et les informations sensibles ne doivent pas être publiés dans le dépôt Git.

## Tests automatisés

Les tests vérifient le bon fonctionnement des fonctionnalités principales et permettent de limiter les régressions après une modification du code.

Ils couvrent notamment :

- La redirection des utilisateurs non connectés vers la page de connexion.
- La création d'un projet et sa sauvegarde dans la base de données.
- La validation du formulaire de tâche lorsqu'un titre est vide.

Pour lancer l'ensemble des tests :

```bash
python manage.py test
```

Django utilise une base de données de test temporaire afin d'exécuter les tests sans modifier les données de développement.

## Choix techniques et difficultés rencontrées

J'ai choisi Django parce qu'il fournit plusieurs fonctionnalités essentielles, comme l'authentification, les formulaires, l'ORM et les migrations. Cela permet de développer une application structurée sans devoir réimplémenter ces mécanismes. L'utilisation de `ModelForm` facilite la validation des données, tandis que les vues génériques permettent de réduire le code nécessaire aux opérations CRUD. J'ai également utilisé des mixins pour centraliser certaines vérifications de permissions et `Django TestCase` pour automatiser les tests.

La principale difficulté a été de gérer correctement les permissions sur les projets et les tâches, tout en veillant à ce qu'un utilisateur ne puisse pas modifier les données d'un autre utilisateur. La gestion des fichiers envoyés par les formulaires et la personnalisation des messages de validation ont également demandé une attention particulière.

Python 3.12 apporte notamment des améliorations du langage et des performances par rapport aux versions antérieures. Django 6.1 fournit les outils nécessaires à la structuration d'une application web moderne, notamment la gestion des modèles, des formulaires, des migrations et des tests. Ces outils contribuent à rendre le code plus maintenable et à faciliter l'évolution du projet.

## Sécurité et bonnes pratiques

- Ne jamais publier de vrais mots de passe ni une `SECRET_KEY` de production dans le dépôt.
- Utiliser des variables d'environnement pour les informations sensibles en production.
- Ne pas désactiver les vérifications de permissions dans les vues CRUD.
- Ne pas versionner l'environnement virtuel `.venv/`.
- Ne pas versionner les fichiers de base de données ou les fichiers médias contenant des données personnelles.
- Conserver les fichiers de migration dans les applications concernées.
- Exécuter les tests après les modifications importantes.


## Conclusion

TaskFlow est un projet de gestion de projets et de tâches qui met en pratique les fonctionnalités fondamentales de Django : modèles, formulaires, vues, authentification, stockage de fichiers, migrations et tests automatisés. Le projet vise à fournir une base claire et maintenable, tout en respectant les bonnes pratiques de développement et de sécurité.