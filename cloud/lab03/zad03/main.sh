#!/bin/bash

docker rm -f nodejs
docker rm -f nginx

docker network rm lab3ex3
docker network create lab3ex3

docker build -t nodejsapp ./app
docker build -t nginxapp ./nginx

docker run -d --name nginx --network lab3ex3 -p 80:80 -p 443:443 nginxapp
docker run -d --name nodejs --network lab3ex3 nodejsapp
