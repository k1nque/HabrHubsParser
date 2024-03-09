python3 -m venv ./.venv
.venv/bin/pip3.12 install -r requirements.txt


.venv/bin/python3.12 ./habrParser/manage.py createsuperuser
.venv/bin/python3.12 ./habrParser/manage.py makemigrations
.venv/bin/python3.12 ./habrParser/manage.py migrate

.venv/bin/python3.12 ./habrParser/manage.py runserver &
.venv/bin/python3.12 scheduler.py &