#!/bin/bash

# bridge is a default driver for docker network
docker network create --driver bridge --subnet 192.168.1.0/24 --gateway 192.168.1.1 lab6ex1

# create a container with the network
docker run --rm -dit --name lab6ex1-main --network lab6ex1 -p 8080:80 busybox

# create a container with the network and ping the first container
docker run --rm --network lab6ex1 busybox ping -c 10 lab6ex1-main
