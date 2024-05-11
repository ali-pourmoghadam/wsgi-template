# wsgi-template
## Build and Run Step by Step :

 1-Build images and network 

- cd <project_dir>/app 

- docker build -t  flaskapp .

- cd <project_dir>/nginx

- docker build -t  mynginx .

- docker network create wsgi-net


2- run images :

- docker run --network wsgi-net --name flaskapp flaskapp

- docker run --network wsgi-net -p 8090:80 mynginx

## Run by Docker-Compose 

in the root of project just enter "docker compose up -d" 

