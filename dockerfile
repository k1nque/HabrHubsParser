FROM python:3.12

WORKDIR /code

ENV PYTHONUNBUFFERED=1
ENV DJANGO_SUPERUSER_PASSWORD=123
ENV DJANGO_SUPERUSER_EMAIL=example@example.com
ENV DJANGO_SUPERUSER_USERNAME=admin

COPY requirements.txt .
COPY main.py .
COPY db.py .
COPY parser.py .
COPY build.bash .
COPY run.bash .
COPY /habrParser ./habrParser

EXPOSE 8000

RUN python3 -m venv ./.venv
RUN .venv/bin/pip3 install -r requirements.txt
RUN chmod ugo+x .venv/bin/python3 
RUN .venv/bin/python3 ./habrParser/manage.py createcachetable
RUN .venv/bin/python3 ./habrParser/manage.py createsuperuser \
        --noinput \
        --username $DJANGO_SUPERUSER_USERNAME \
        --email $DJANGO_SUPERUSER_EMAIL
RUN .venv/bin/python3 ./habrParser/manage.py makemigrations
RUN .venv/bin/python3 ./habrParser/manage.py migrate

CMD bash run.bash