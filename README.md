## Sample Flask app to run in GCP Cloud run
[![cloud build status](https://storage.googleapis.com/sample-gcp-app-cicd/build/sample-gcp-app-master-badge.svg)](https://github.com/Porkbutts/sample-gcp-app)

Just a simple flask app for now.

## Build
Create a virtual python environment.
```
virtualenv venv
source venv/bin/activate
```

Install requirements
```
pip install -r requirements.txt
```

## Run
The application requires a mongodb database and is configured to find one over `localhost` by default.
The app is exposed on whatever port the `PORT` environment variable is set to, or `8080` if not set.

### Run web tier and mongodb using docker-compose
```
docker-compose up
```

### Run with Python
This assumes you have mongodb running on `localhost`.
```
PORT=80 python app.py
```

Then visit on something like http://localhost

## Deploy
Whenever commits are pushed to the `master` or `develop` branch, Google Cloud will detect this and run the steps outlined in `cloudbuild-production.yaml` or `cloudbuild-staging.yaml` respectively. The built image will be deployed to Google Cloud Run as follows.

- `(master)` http://cloudrun-demo.tengamnuay.me
- `(develop)` http://cloudrun-demo-staging.tengamnuay.me
