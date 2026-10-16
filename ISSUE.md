# 🏷️ Titre : [Test Technique Stagiaire] Développement de "TaskFlow" - Gestionnaire de tâches collaboratif (Django)

## 📝 Contexte et Objectifs

Dans le cadre de votre stage, nous souhaitons évaluer vos compétences sur le framework **Django**. Vous devez développer une petite application nommée **"TaskFlow"**.

L'objectif n'est pas d'avoir une UI parfaite, mais de démontrer que vous maîtrisez les fondamentaux de Django (URLs, vues et templates, modèles et ORM, migrations, formulaires, authentification, sécurité, etc.) et que vous écrivez un code propre, moderne et maintenable.

> 💡 Ce dépôt ne contient **volontairement aucun code** : vous devez initialiser le projet vous-même (US1), puis implémenter les user stories les unes après les autres. Les seuls fichiers fournis sont ce document, le `README.md` et le workflow d'intégration continue.

## ⏱️ Durée estimée

**4 à 6 heures** (À réaliser seul(e), sans aide extérieure ni copie de code existant).

## 🛠️ Prérequis techniques

* **Python 3.12** ou plus récent, et `pip` installés.
* **Django 6.1** : installez-le dans un environnement virtuel et figez la version dans `requirements.txt` (n'ajoutez aucun autre framework).
* Utilisation de **SQLite** (pour faciliter la configuration de la base de données sans avoir à installer MySQL/PostgreSQL).
* L'authentification doit être mise en place **par vos soins** à l'aide de `django.contrib.auth` (fourni avec Django) : aucun package tiers n'est nécessaire.

---

## 📋 User Stories et Critères d'Acceptation

Veuillez cocher les cases au fur et à mesure de votre avancement en faisant des commits réguliers.

### US1 : Initialisation du projet et Authentification

**En tant que** visiteur
**Je veux** pouvoir m'inscrire et me connecter
**Afin de** accéder à mon espace personnel.

- [ ] **CA1 :** Le projet Django 6.1 est initialisé (`django-admin startproject config .`), les dépendances sont figées dans un `requirements.txt` à la racine et la base de données SQLite est configurée dans `config/settings.py`.
- [ ] **CA2 :** L'authentification est mise en place à l'aide de `django.contrib.auth` : inscription (formulaire + vue), connexion, déconnexion, et un layout de pages minimal.
- [ ] **CA3 :** Les routes `/login/`, `/register/` et `/logout/` (noms `login`, `register`, `logout`) fonctionnent correctement, et la page protégée de votre espace (`/dashboard/` ou `/projects/`) redirige un visiteur non connecté vers la page de connexion.

### US2 : Gestion des Projets (CRUD)

**En tant que** utilisateur connecté
**Je veux** créer, lister, modifier et supprimer des projets
**Afin d'** organiser mes tâches.

- [ ] **CA1 :** Une migration `projects` est créée avec les champs : `id`, `user` (clé étrangère vers l'utilisateur créateur, `on_delete=models.CASCADE`), `name` (`CharField`), `description` (`TextField`, nullable), `created_at`, `updated_at`.
- [ ] **CA2 :** Un modèle `Project` est créé avec la relation `ForeignKey(User, on_delete=models.CASCADE, related_name='projects')`.
- [ ] **CA3 :** Le modèle `User` possède la relation inverse (accès à `user.projects`) et un projet peut être retrouvé depuis son propriétaire.
- [ ] **CA4 :** Les routes sont définies dans un fichier dédié (ex : `projects/urls.py`) et incluses dans `config/urls.py` ; elles sont protégées par l'authentification (`LoginRequiredMixin` ou `@login_required`).
- [ ] **CA5 :** Des vues de type "resource" (`ProjectListView`, `ProjectCreateView`, `ProjectUpdateView`, `ProjectDeleteView` — CBV génériques ou vues fonctionnelles) sont utilisées pour lister, créer, modifier et supprimer.
- [ ] **CA6 :** L'utilisateur ne peut voir/modifier/supprimer que ses **propres** projets (filtrage systématique du `QuerySet` par `self.request.user` ou utilisation d'un `Manager`/`QuerySet` personnalisé).

### US3 : Gestion des Tâches avec Validation

**En tant que** utilisateur connecté
**Je veux** ajouter des tâches à mes projets avec un statut
**Afin de** suivre leur avancement.

- [ ] **CA1 :** Une migration `tasks` est créée : `id`, `project` (clé étrangère), `title` (`CharField(max_length=255)`), `status` (`TextChoices` : `pending`, `in_progress`, `done`), `deadline` (`DateField`, nullable), `created_at`, `updated_at`.
- [ ] **CA2 :** Un modèle `Task` avec les relations appropriées (`Task.project` et `Project.tasks`).
- [ ] **CA3 :** La création et la modification d'une tâche utilisent un **formulaire** (`TaskForm` dans `forms.py`, `forms.ModelForm`).
- [ ] **CA4 :** Les règles de validation imposent : `title` obligatoire (max 255 caractères), `status` obligatoire (doit être l'une des 3 valeurs), `deadline` doit être une date valide.
- [ ] **CA5 :** En cas d'échec de validation, les erreurs s'affichent clairement dans le template (`{{ form.field.errors }}`) et l'ancienne saisie est conservée (réaffichage du formulaire lié, ex. `{{ form.title.value }}` / `value="{{ form.title.value|default:'' }}"`).

### US4 : Templates et Héritage de templates

**En tant que** utilisateur
**Je veux** avoir une interface claire et cohérente
**Afin de** naviguer facilement dans l'application.

- [ ] **CA1 :** Création d'un layout principal (ex : `templates/layouts/app.html` ou `templates/base.html`) contenant les blocs `{% block content %}` / `{% block title %}`, et les pages du projet étendent ce layout avec `{% extends %}`.
- [ ] **CA2 :** Utilisation de **templates réutilisables** (`{% include %}` ou un `inclusion_tag` personnalisé) — par exemple un bloc `_alerts.html` — pour afficher les messages de succès ou d'erreur de façon réutilisable (framework `django.contrib.messages`).
- [ ] **CA3 :** Sur la page de détail d'un projet, les tâches sont affichées dans un tableau avec un formulaire pour changer le statut rapidement.

### US5 : Sécurité et Autorisation (Logique métier)

**En tant qu'** administrateur système (Contrainte technique)
**Je veux** m'assurer qu'un utilisateur ne peut pas interagir avec un projet qui ne lui appartient pas
**Afin de** garantir la sécurité des données.

- [ ] **CA1 :** Création d'un **mixin (ou d'un décorateur) réutilisable** `ProjectOwnerRequiredMixin` (équivalent du middleware `EnsureUserOwnsProject` d'autres frameworks), placé dans un module dédié (ex : `projects/mixins.py`).
- [ ] **CA2 :** Le mixin vérifie que le projet demandé appartient bien à l'utilisateur authentifié. Si non, il retourne une erreur **403** (`from django.core.exceptions import PermissionDenied` ou `HttpResponseForbidden`).
- [ ] **CA3 :** Le mixin est appliqué sur les vues de modification/suppression des projets **et** sur les vues de création/modification/suppression des tâches associées.

### US6 : Fonctionnalités avancées de l'ORM (Scopes & Accessors)

**En tant qu'** utilisateur
**Je veux** voir mes tâches triées et formatées proprement
**Afin de** gagner du temps dans ma lecture.

- [ ] **CA1 :** Création d'un **QuerySet/Manager personnalisé** sur le modèle `Task` permettant de filtrer les tâches en retard : `Task.objects.overdue()` (équivalent d'un local scope).
- [ ] **CA2 :** Création d'une **propriété / accesseur** sur le modèle `Task` pour formater le statut en français (ex : si `status` est `pending`, `task.status_label` retourne "En attente").
- [ ] **CA3 :** Utilisation de l'**eager loading** (`select_related()` / `prefetch_related()`) lors de la récupération des projets et de leurs tâches pour éviter le problème des requêtes N+1.

### US7 : Upload de fichiers (Storage)

**En tant qu'** utilisateur
**Je veux** pouvoir attacher une pièce jointe à une tâche
**Afin de** fournir des documents complémentaires.

- [ ] **CA1 :** Ajout d'un champ `attachment` (`FileField`, `upload_to='attachments/'`, nullable, blank) dans le modèle `Task` et sa migration.
- [ ] **CA2 :** Sur le formulaire de création de tâche, ajout d'un input de type `file` (`enctype="multipart/form-data"`).
- [ ] **CA3 :** Le stockage est configuré dans `config/settings.py` (`MEDIA_URL` et `MEDIA_ROOT`) et le fichier est enregistré sur le disque via le stockage de fichiers de Django, dans un sous-dossier `attachments`.
- [ ] **CA4 :** Le lien de téléchargement de la pièce jointe s'affiche sur la vue de la tâche (`task.attachment.url`). Les fichiers de `MEDIA_ROOT` doivent être servis en développement (`static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)` dans `config/urls.py`).

### US8 : Tests unitaires et fonctionnels (Django TestCase)

**En tant que** développeur
**Je veux** m'assurer que mes fonctionnalités clés fonctionnent
**Afin de** prévenir les régressions.

- [ ] **CA1 :** Écriture d'un test fonctionnel pour vérifier qu'un utilisateur non connecté est redirigé vers la page de connexion s'il tente d'accéder aux projets.
- [ ] **CA2 :** Écriture d'un test fonctionnel pour vérifier la création réussie d'un projet dans la base de données.
- [ ] **CA3 :** Écriture d'un test fonctionnel pour vérifier que les règles de validation échouent si le `title` de la tâche est vide.

---

## 📦 Livrables attendus

1. **Dépôt Git (GitHub/GitLab) :** contenant l'intégralité du code source.
2. **Configuration de la base de données :** SQLite configurée dans `config/settings.py` (`ENGINE: django.db.backends.sqlite3`) et dépendances figées dans `requirements.txt`. *(Attention : ne jamais commiter de vrais mots de passe ou une `SECRET_KEY` de production dans `settings.py`).*
3. **Fichiers de migration :** versionnés dans les applications concernées (`projects/migrations/`, `tasks/migrations/`).
4. **Fichier `README.md` :** à la racine du projet, contenant :
    *   Les instructions pour lancer le projet (`python -m venv .venv`, `pip install -r requirements.txt`, `python manage.py migrate`, `python manage.py runserver`, etc.).
    *   Un petit paragraphe expliquant vos choix techniques (pourquoi vous avez utilisé tel pattern, quelle a été votre plus grande difficulté, ce que vous apporte Python 3.12 / Django 6.1 dans ce contexte, etc.).

## 🚫 Consignes strictes

*   **Aucun package frontend tiers (React, Vue, Alpine, Tailwind, htmx, etc.) n'est autorisé.** Nous voulons du pur **template Django / HTML / CSS basique**.
*   **Aucun package d'administration ou d'UI tiers (Django Jet, django-admin-interface, django-unfold, DRF pour les vues, etc.).** L'admin Django intégré reste bien sûr disponible.
*   Le code doit respecter les standards **PEP 8** (formatez votre code avec `black .` et vérifiez-le avec `ruff check .`).
*   Les tests doivent être exécutables avec la commande `python manage.py test`.
*   Le workflow d'intégration continue fourni (`.github/workflows/django-tests.yml`) exécute `python manage.py check` puis `python manage.py test` : il ne passera qu'une fois le projet créé à la racine du dépôt.

## 💡 Conseils pour réussir

*   Commencez par l'**US1** : le dépôt ne contient aucun code, c'est à vous d'initialiser le projet.
*   Faites des **commits petits et fréquents** (ex : un commit par User Story). Nous regarderons l'historique Git !
*   Pensez à la réutilisation de votre code (DRY - Don't Repeat Yourself), notamment pour la vérification des droits et l'affichage des messages.
*   Ne bloquez pas 2 heures sur du CSS, l'important est le backend et la logique Django.
*   En cas de blocage sur une US, passez à la suivante et documentez votre blocage dans le README.

Bon courage ! 🚀
