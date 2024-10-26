#! /bin/bash

APP_NAME="cg-api"
APP_VERSION="latest"
DOCKER_FILE="cicd/docker/Dockerfile"
SOURCE_FILE="cicd/docker/sources.list"

docker build --no-cache -f $DOCKER_FILE \
  -t $APP_NAME:$APP_VERSION .

docker save > C://temp/cg-api.tar $APP_NAME:$APP_VERSION