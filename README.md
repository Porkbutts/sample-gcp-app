## Sample Flask app to run in GCP Cloud run
[![cloud build status](https://storage.googleapis.com/sample-gcp-app-cicd/build/sample-gcp-app-master-badge.svg)](https://github.com/Porkbutts/sample-gcp-app)

Just a simple flask app for now.

## Requirements


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
As required by **Google Cloud Run**, the app is exposed on whatever port the `PORT` environment variable is set to, or `8080` if not set.
The app depends on **Google Cloud Firestore** `(TODO: Instructions for developing with firestore)`.

### Run with Python
Start the web tier
```
PORT=80 python app.py
```

Visit on something like http://localhost

## Deploy
Whenever commits are pushed to the `master` or `develop` branch, Google Cloud will detect this and run the steps outlined in `cloudbuild-production.yaml` or `cloudbuild-staging.yaml` respectively. The built image will be deployed to Google Cloud Run as follows.

- `(master)` http://cloudrun-demo.tengamnuay.me
- `(develop)` http://cloudrun-demo-staging.tengamnuay.me
