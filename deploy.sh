#!/bin/bash

# Set the Docker image name and version
IMAGE_NAME="my-app"
IMAGE_VERSION="1.0.0"

# Build the Docker image
docker build -t $IMAGE_NAME:$IMAGE_VERSION .

# Tag the Docker image with latest
docker tag $IMAGE_NAME:$IMAGE_VERSION $IMAGE_NAME:latest

# Push the Docker image to Docker Hub
docker push $IMAGE_NAME:$IMAGE_VERSION
docker push $IMAGE_NAME:latest

# Deploy the Docker image using Docker Compose
docker-compose up -d
