
# Wildlife Tracker

This is a web app built in python + django + javascript aimed at tracking encounters with local wild life. Map is built with leaflet + Map Box tiles. Basic geospatial CRUD app that saves report location to database and returns to webpage.

## Motivation
Living in an urban environment can make one forget how closely related we are to the world outside. Many Bay Area communities are nestled against rolling hills and expansive wild lands that are home to a host of wild life. These habitats are home to prey driven wildlife, some of which, are apex predators like the mountain lion.

The SfBayWildlifeTracker represents a collaboration by Kickstart Coding students Masa Yana, Joseph Reid, and Mathew Cubell. The purpose of this project was to create a fully functioning, web based application that incorporated the Frontend and Backend development concepts which were taught during the first eight weeks of a sixteen week Fullstack coding boot camp.

## Setup

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

3. Migrate

```
python3 manage.py Migrate
```

4. Run Server
```
python3 manage.py runserver
```
Default address is `localhost:8000`

## Licence
TBD
