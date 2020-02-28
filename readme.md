# Theodo test - Strava POC

Expose basic API endpoints permitting to manage running statistics per user.

## Requirements

- Have Python >= 3.7 installed

## Install

1. git clone the project :

```bash
git clone git@github.com:NeilujD/theodo_test.git
```


2. install dependencies :

```bash
pip install -r requirements.txt
```


3. run migrations :

```bash
pip manage.py migrate
```

## Run locally

1. use `SECRETE_KEY` environment variable ([see Django docs](https://docs.djangoproject.com/fr/3.0/ref/settings/#secret-key))


2. Start the server

```bash
python manage.py runserver
```

## How to use

1. Create an user :
```bash
python manage.py createsuperuser
```


2. Retrieve a token using the `/api/token-auth/` endpoint :

- body parameters :
    - `username` : your user username
    - `password` : yout user password
- response body :
    - `token` : your user token


3. Use `/api/runs/` endpoint :
- set the `Authorization` header as `Token <your_token>`
- create a run :
    - `start_date` : the run start date and time (`DateTime`)
    - `end_date` : the run end date and time (`DateTime`)
    - `distance` : the run distance in km (`Float`)
    - `burnt_calories`: the burnt calories amount during the run (`Integer`)