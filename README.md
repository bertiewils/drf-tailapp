# About the app

A few models were created for flexibility:

- FootballTeam
- Stadium
- League

A football team can belong to a stadium and a league;
a stadium or a league can have multiple teams.

The initial teams are loaded from `fixtures/initial_data.yaml`.


# Running the API with Docker

    docker-compose build
    docker-compose run app python manage.py createsuperuser \
        --email radu@localhost --username radu
    docker-compose up app


# Running the tests with Docker

    # docker-compose build
    docker-compose run tests


# Installing and running the app directly

We assume `python3` is used.

    python -m venv venv
    source venv/bin/activate
    pip install -U pip && pip install -r requirements.txt

    python manage.py migrate
    python manage.py loaddata fixtures/initial_data.yaml
    python manage.py createsuperuser --email radu@localhost --username radu

    python manage.py test
    python manage.py runserver

# The API

The API can be reached at:

<http://localhost:8000/api/v1/>
