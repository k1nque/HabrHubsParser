.venv/bin/python3 ./habrParser/manage.py runserver 0.0.0.0:8000 &
.venv/bin/python3 main.py &

wait -n
exit $?