
# Wildlife Tracker

This is a web app built in python + django + javascript aimed at tracking encounters with local wild life. Map is built with leaflet + Map Box tiles. Basic geospatial CRUD app that saves report location to database and returns to webpage.

## Motivation
Living in an urban environment can make one forget how closely related we are to the world outside. Many Bay Area communities are nestled against rolling hills and expansive wild lands that are home to a host of wild life. These habitats are home to prey driven wildlife, some of which, are apex predators like the mountain lion.

The SfBayWildlifeTracker represents a collaboration by Kickstart Coding students Masa Yana, Joseph Reid, and Mathew Cubell. The purpose of this project was to create a fully functioning, web based application that incorporated the Frontend and Backend development concepts which were taught during the first eight weeks of a sixteen week Fullstack coding boot camp.



## Local Setup

1. Clone Repo

```
git clone git@github.com:sudo-joseph/wildlife_tracker.git
```

2. Setup Virtual Env:

```
pipenv --python 3

pipenv install

pipenv shell
```

Note: psycog2-binary will not install in local environment and will throw error during `pipenv install`.

3. Migrate

```
python3 manage.py migrate
```

4. Run Server
```
python3 manage.py runserver
```
Default address is `localhost:8000`

## Dependencies
```
[packages]
django = "*"
django-bootstrap4 = "*"
django-heroku = "*"
gunicorn = "*"
psycopg2-binary = "*"
django-crispy-forms = "*"
geopy = "*"
boto3 = "*"
django-storages = "*"

[dev-packages]
django-debug-toolbar = "*"
pylint = "*"
v = {editable = true,version = "*"}
```
### Secrets
Site requires .env secrets file. See .env.example for format. Site requires mapbox API public and private API tokens for full functionality. See https://docs.mapbox.com/help/how-mapbox-works/access-tokens/

## Licence
TBD
