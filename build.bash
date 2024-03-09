python3 -m venv ./.venv
.venv/bin/pip3 install -r requirements.txt


.venv/bin/python3 ./habrParser/manage.py createsuperuser
.venv/bin/python3 ./habrParser/manage.py makemigrations
.venv/bin/python3 ./habrParser/manage.py migrate