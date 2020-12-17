# wicgate-backend

Backend Service for WicGate

## Table of Contents

1. [Introduction](#1-Introduction)
2. [Setup](#2-Setup)
3. [Usage](#3-Usage)
4. [Deployment](#4-Deployment)
5. [Testing](#5-Testing)
6. [Styles](#6-Styles)

---

## 1. Introduction

The old massgate is dead, that's why this is happening: **WicGate**

---

## 2. Setup

### 2.1. Prerequisites

You should have the following installed:

- Python3 (the currently used python version can be found in `runtime.txt`)
- Postgresql server & client

### 2.2. Install Requirements

Python requirements are located in the `requirements` directory. You will find three files, `base.txt`, `local.txt` and `production.txt`.

Note: The `requirements.txt` in the root directory is just a chained called, that is used **by Heroku**. Do not use this file, you might miss dev dependencies. Therefore:

```bash
pip install -r requirements/local.txt
```

Every subsequent step is purely optional and (may be) for your convenience.

### 2.3. Django Settings (optional)

In case you need to make changes to Django's settings, you can find detailed information [here](https://docs.djangoproject.com/en/3.0/ref/settings/) and [here](https://docs.djangoproject.com/en/3.0/topics/settings/).

TODO:
`Settings.py` files can be found under `config/settings`, which holds a dedicated file for each environment.

[Avaliable settings.py paramater set via cookiecutter](http://cookiecutter-django.readthedocs.io/en/latest/settings.html)

### 2.4. Environment Variables (optional)

Env Variables are located in the `.envs` directory.

TODO:
Important: You can **NEVER** store/commit any credentials in the repository. Those files are ignored by git. However, in order to handle envs transparently, a `template.env` file is included. This file holds all keys that are actively used. Changes to this file can be commited. However, keep in mind to **NEVER** commit any sensitive information. Just leave the values blank.

Usage:

1. **Copy** all the keys from the `template.env` file to your `local.env` file and **set** the values for each key accordingly.
2. You need to expose the env variables to the execution context (see 5).
3. If you start the application with your IDE, make sure it loads all variables.
4. Use your preferred way of exposing env vars to your shell. However, a `.envrc` file is provided, which can be used by [direnv](https://direnv.net/) to automatically load all variables into the shell whenever you `cd` into the directory.
5. Otherwise, you just can expose the variables via `export $(xargs < .envs/local.env)`.

Note: Heroku manages all environment variables via their "settings tab". This effectively means, that you have to set the variables in Heroku. The respective `*.env` file is just for local development and in case you want to debug against a certain stage form your local machine (e.g. database access, scripts, whatever).

### 2.5. Database Setup (optional)

This is only required if you want to access a dedicated postgres instance/database for development. If you're good to go with the default postgres, just skip this section.

TODO:
The configuration applied here should reflect the `$DATABASE_URL` env variable in `template.env` (make a `local.env` copy of that file).

```bash
sudo su – postgres
psql  # This will put you in the psql shell

CREATE DATABASE wicgate_backend; # Create the database
CREATE USER wicgate_backend WITH PASSWORD 'YOUR_PASSWORD'; # Create a distinct user for this database
GRANT ALL PRIVILEGES ON DATABASE wicgate_backend TO wicgate_backend; # Grant all priviliges to this particular user and database

\q # Exit psql shell
exit # Exit root user

psql -U wicgate_backend -h localhost -p 5432 -d wicgate_backend # Verify everything is working (port and host are up to your configuration)
```

In case you may receive a `django.db.utils.ProgrammingError: permission denied for relation django_migrations` : [stackoverflow](https://stackoverflow.com/questions/38944551/steps-to-troubleshoot-django-db-utils-programmingerror-permission-denied-for-r)

---

### 2.6. Email Server (optional)

In development, it is often nice to be able to see emails that are being sent from your application. If you choose to use `MailHog`\_ when generating the project a local SMTP server with a web interface will be available.

- `Download the latest MailHog release`\_ for your OS.
- Rename the build to `MailHog`.
- Copy the file to the project root.
- Make it executable: `$ chmod +x MailHog`
- Spin up another terminal window and start it there: `./MailHog`
- Check out `<http://127.0.0.1:8025/>`\_ to see how it goes.

Now you have your own mail server running locally, ready to receive whatever you send it.

- `Download the latest MailHog release`: https://github.com/mailhog/MailHog/releases

### 2.7. Sentry (optional)

Sentry is an error logging aggregator service. You can sign up for a free account at https://sentry.io/signup/?code=cookiecutter or download and host it yourself.
The system is setup with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.

---

## 3. Usage

### 3.1. Database Initialization

```python
python manage.py migrate  # Setup db tables for django
```

**Optional**: If you wish to populate the database with a default set of feeds, run:

```bash
python manage.py curated_feeds
```

### 3.2. Starting the Server

```python
python manage.py runserver  # Runs under http://127.0.0.1:8000/
```

### 3.3. Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create an **superuser account**, use this command:

  ```
  python manage.py createsuperuser
  ```

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### 3.4. Live reloading and Sass CSS compilation

[Live reloading and SASS compilation](http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html)

---

## 4. Deployment

The following details how to deploy this application.

### 4.1. Heroku

[cookiecutter-django Heroku documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html)

#### Environment Variables

Following environment variables need to be set in heroku:

- DJANGE_SECRET_KEY (e.g. A98AOE8O#12WV)
- DJANGO_ALLOWED_HOSTS (e.g. wicgate-staging.herokuapp.com)
- DATABASE_URL (automatic)
- REDIS_URL (automatic)

#### Build & Deployment

Deployment works like this:

- Whenever you merge a pull request into `master` it automatically gets deployed to **staging**.
- Each time you merge into `production` it will automatically deploy to **production**.
- (Every time you open up a new pull request, it will automatically create a dedicate app for this sole PR with a dedicated URL. Mulitple PR-Stages can exist next to each other.) not yet

---

## 5. Testing

### 5.1. Type checks

Running type checks with mypy:

```bash
mypy wicgate
```

### 5.2. Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

```bash
coverage run -m pytest
coverage html
open htmlcov/index.html
```

### 5.3. Running tests with py.test

```bash
pytest
```

---

## 6. Styles

### 6.1. EditorConfig

Make sure you editor of choice supports [EditorConfig](https://editorconfig.org/).

### 6.2. flake8, pylint, pycodestyle

TODO: black? bandit? yapf? autopep8? [summary](https://books.agiliq.com/projects/essential-python-tools/en/latest/linters.html)

#### flake8

[flake8](https://flake8.pycqa.org/en/latest/) is a wrapper around these tools:

- PyFlakes
- pycodestyle
- Ned Batchelder's McCabe script

```bash
flake8 # Runs flake8 on the whole project
flake8 path/to/dir/or/file  # Runs flake8 on the specified directory or file
```

Ignoring error messages:

```bash
// In order to ignore a rule for the whole file put a noqa statement at the top of the file
# flake8: noqa E731,E123

// If you only want to exclude a single line, post-comment it like this:
y = 6  # noqa: ABC456,E123  # TODO: will fix this later
```

Flake8's [configuration](https://flake8.pycqa.org/en/latest/user/configuration.html) is stored in `.flake8` file.

Note: Flake8 highly depends on the underlying python version. Make sure that you execute flake8 with the correct python interpreter (see `runtime.txt`).

#### pycodestyle

[pycodestyles](https://pycodestyle.pycqa.org/en/latest/) is a tool to check your Python code against some of the style conventions in [PEP 8](https://www.python.org/dev/peps/pep-0008/). It will be executed as part of flake8. However, you can execute it separately if you want (refer to the docu).

#### pyflakes

[Pyflakes](https://github.com/PyCQA/pyflakes) analyzes programs and detects various errors. It works by parsing the source file, not importing it, so it is safe to use on modules with side effects. It will be executed as part of flake8.

#### pylint

[pylint](https://www.pylint.org/)

### 6.3. Isort

[isort](https://github.com/timothycrosley/isort) ensures consistent `import` ordering.

```bash
isort  # Runs isort against the repository (interactively)
```

---

## 7. API

- [http://localhost:8000/api/](http://localhost:8000/api/)

## 8. Django

- [https://djangoadventures.com/how-to-integrate-django-with-existing-database/](https://djangoadventures.com/how-to-integrate-django-with-existing-database/)
- [https://www.webforefront.com/django/modelmultidatabases.html](https://www.webforefront.com/django/modelmultidatabases.html)

## 9. Timeline

- [https://codepen.io/Maxalos/pen/MXXqGj](https://codepen.io/Maxalos/pen/MXXqGj)
