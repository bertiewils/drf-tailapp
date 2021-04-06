FROM python:3.9.2-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /opt/app
COPY requirements.txt /opt/app/

RUN pip install -U pip && \
    pip install -r requirements.txt

COPY . /opt/app

RUN python3 manage.py migrate && \
    python3 manage.py loaddata fixtures/initial_data.yaml

# Create a default superuser
RUN python3 manage.py create-superuser --username radu1 --email radu1@localhost --password radu1

CMD python3 manage.py runserver 0.0.0.0:8000
