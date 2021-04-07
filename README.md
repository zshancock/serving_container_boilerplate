# Serving Container Boilerplate

## Introduction
A starter container that utilizes guinicorn and Falcon to create a serving instance. This starter container has two routes `health` and `predict`. The `predict` route is currently a placeholder for a more complicated prediction routine, and currently only doubles the value of requested integer.

## Prerequisites
- Docker
- flake8
- pytest


## Running container locally using cURL

The container is exposed on port 8000, start with:
```sh
make serving.run
```
Then in a new terminal, use the service. First, examine the `health` route to ensure container is running properly:
```sh
curl http://0.0.0.0:8000/health
```
Returns - `Healthy`

Now make a request to the service. Currently the expected response is formatted as one field of `request` with any integer:
```sh
curl -d '{"request":3}' -H 'Content-Type: application/json' http://0.0.0.0:8000/predict
```
Returns - `{"response": 6}`

Kill the serving container with `CONTROL+Z`. Then clear port 8000 with:
```sh
make clean
```

## Testing and Linting
Test with:
```sh
python -m pytest
```

Linting:
```sh
python -m flake8
```

## Extra - Using AI Platform's Custom Container
I have had success with serving custom containers on GCP's AI Platform, by first tagging the container and pushing to Artifact Registry. [Custom Container Documentation for AI Platform](https://cloud.google.com/ai-platform/prediction/docs/use-custom-container). 
Example upload:
```sh
gcloud beta ai-platform versions create {VERSION_NAME} --region=us-central1 --model={MODEL} --machine-type=n1-standard-4 --accelerator=type=nvidia-tesla-t4,count=1 --image={image_name}:latest --ports=8000 --health-route=/health --predict-route=/predict
```
