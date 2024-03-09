python3 ./habrParser/manage.py makemigrations
python3 ./habrParser/manage.py migrate

nohup python3 ./habrParser/manage.py runserver

python3 scheduler.py