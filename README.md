You can configure admin_nickname and admin_password in dockerfile.

To start the app you need:
 > 1. docker build .
 > 2. docker run -p 8000:8000 [docker_container_id]

The service will be available by http://0.0.0.0:8000/admin

To parse a hub, you need to add hub name in the table in admin-panel.

You enter hub's table, and enter the name of hub inside the text field. 

You can find the right hub's name in the URL string as on example image:
![alt text](https://github.com/k1nque/HabrHubsParser/blob/master/images/hub_name.jpg?raw=true)

