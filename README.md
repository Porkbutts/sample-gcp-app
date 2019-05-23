## Sample Flask app to run in GCP Cloud run
[![cloud build status](https://storage.googleapis.com/sample-gcp-app-cicd/build/sample-gcp-app-master-badge.svg?branch=master)](https://github.com/Porkbutts/sample-gcp-app)

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
You can run with python or with Docker. The app is exposed on whatever port the `PORT` environment variable is set to, or `8080` if not set.

### Python
```
python app.py
```

### Docker
```
docker build -t sample-gcp-app:latest .
docker run -ti --rm 8080:8080 sample-gcp-app:latest
```

Then visit on something like http://localhost:8080

## Deploy
The `cloudbuild.yaml` file tells GCP to build the docker image, then push it up to Google Container Registry.
Lastly it kicks off a deploy to Google Cloud Run.
