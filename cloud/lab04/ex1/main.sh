#!/bin/bash

docker rm -f lab4ex1

mkdir nginx_data

docker run -d \
    --name lab4ex1 \
    -p 80:80 \
    -v ./nginx_data:/usr/share/nginx/html \
    nginx

echo "The change was succesfull" >nginx_data/index.html
