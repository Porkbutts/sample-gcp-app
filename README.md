## Sample Flask app to run in GCP Cloud run
Just a simple flask app for now.

## Run

### Python
```
python app.py
```

### Docker
```
docker build -t sample-gcp-app:latest .
docker run -ti --rm 5000:5000 sample-gcp-app:latest
```

## Build
The `cloudbuild.yaml` file tells GCP to build the docker image, then push it up to Google Container Registry.
Lastly it kicks off a deploy to Google Cloud Run.