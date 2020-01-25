#!/bin/bash
docker build -t business-facilities .
docker run \
  -it \
  --rm \
  -p 4200:80 \
  -v $PWD/app:/usr/src/app \
  -v $PWD/data:/usr/src/data \
  --env-file=.env \
  business-facilities