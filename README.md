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

---

### 2.1. Settings & Config

- [Avaliable settings.py paramater set via cookiecutter](http://cookiecutter-django.readthedocs.io/en/latest/settings.html)

### 2.2. Email Server

In development, it is often nice to be able to see emails that are being sent from your application. If you choose to use `MailHog`\_ when generating the project a local SMTP server with a web interface will be available.

- `Download the latest MailHog release`\_ for your OS.
- Rename the build to `MailHog`.
- Copy the file to the project root.
- Make it executable: `$ chmod +x MailHog`
- Spin up another terminal window and start it there: `./MailHog`
- Check out `<http://127.0.0.1:8025/>`\_ to see how it goes.

Now you have your own mail server running locally, ready to receive whatever you send it.

- `Download the latest MailHog release`: https://github.com/mailhog/MailHog/releases

### 2.3. Sentry

Sentry is an error logging aggregator service. You can sign up for a free account at https://sentry.io/signup/?code=cookiecutter or download and host it yourself.
The system is setup with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.

---

## 3. Usage

---

### 3.1. Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create an **superuser account**, use this command:

  ```
  python manage.py createsuperuser
  ```

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### 3.2. Live reloading and Sass CSS compilation

[Live reloading and SASS compilation](http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html)

---

## 4. Deployment

The following details how to deploy this application.

### 4.1. Heroku

[cookiecutter-django Heroku documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html)

Following environment variables need to be set in heroku:

- DJANGE_SECRET_KEY (e.g. A98AOE8O#12WV)
- DJANGO_ALLOWED_HOSTS (e.g. wicgate-staging.herokuapp.com)
- DATABASE_URL (automatic)
- REDIS_URL (automatic)

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
