<h1 align="center">Basic Catalog System - API</h1>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Built Using](#built_using)
- [Authors](#authors)

## 🧐 About <a name = "about"></a>

Challenge basic catalog system to manage products. A product should have basic info such as sku, name, price and brand.

In this system, we need to have at least two type of users: (i) admins to create / update / delete products and to create / update / delete other admins; and (ii) anonymous users who can only retrieve products information but can't make changes.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to create a virtualenv

```
python -m venv env
```

### Installing

Install requirements

```
pip install -r requirements.txt
```

Create database migrations

```
python manage.py makemigrations
python manage.py migrate
```

## 🔧 Running the tests <a name = "tests"></a>

```
pytest
```

## 🚀 Deployment <a name = "deployment"></a>

Now, we need to run our server

```
python manage.py runserver
```

## ⛏️ Built Using <a name = "built_using"></a>

- [SQLite](ttps://www.sqlite.org) - Database
- [Django RestFramework](https://www.django-rest-framework.org/) - Server Framework
- [Django](https://www.djangoproject.com/) - Server Environment
- [Swagger](https://swagger.io/) - Documentation
- [Pytest](https://pytest.org/) - Testing

## ✍️ Authors <a name = "authors"></a>

- [@csampedroc](https://github.com/csampedroc)
