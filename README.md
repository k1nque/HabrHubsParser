You can configure admin_nickname and admin_password in dockerfile.

To start the app you need:
 > 1. docker build .
 > 2. docker run -p 8000:8000 [docker_container_id]

The service will be available by http://0.0.0.0:8000/admin
