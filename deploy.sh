#!/bin/bash

git reset --hard HEAD
git pull
docker stop $(docker ps -a -q)
docker container prune --force
docker rmi nekobot --force
docker build -t nekobot .
docker run -d nekobot
