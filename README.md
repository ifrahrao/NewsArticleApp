# NewsArticleApp

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/ifrahrao/NewsArticleApp.git
$ cd NewsArticleApp
```

Create a virtual environment to install dependencies in and activate it:
```sh
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Make Migrations
```sh
python -m manage migrate
```
## Create Superuser Admin
```sh
python -m manage createsuperuser
```

## Run Server
```sh
python manage.py runserver
```