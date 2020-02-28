# Theodo test - Strava POC

Expose basic API endpoints permitting to manage running statistics per user.

## Requirements

- Have Python >= 3.7 installed

## Install

1. git clone the project (TODO : add the clone command line)
2. install dependencies :
```bash
pip install -r requirements.txt
```

## Run locally

1. use `SECRETE_KEY` environment variable ([see Django docs](https://docs.djangoproject.com/fr/3.0/ref/settings/#secret-key))


2. Start the server
```bash
python manage.py runserver
```