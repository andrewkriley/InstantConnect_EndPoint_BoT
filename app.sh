#!/bin/bash
docker stop webex-webhook
docker container prune
docker build --tag webex-webhook-docker .
docker run -d --name webex-webhook --publish 5005:5005 webex-webhook-docker

