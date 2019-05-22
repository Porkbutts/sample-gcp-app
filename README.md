## Sample Flask app to run in GCP Cloud run
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
You can run with python or with Docker. The app is exposed on port 5000.

### Python
```
python app.py
```

### Docker
```
docker build -t sample-gcp-app:latest .
docker run -ti --rm 5000:5000 sample-gcp-app:latest
```

Then visit on something like http://localhost:5000

## Deploy
The `cloudbuild.yaml` file tells GCP to build the docker image, then push it up to Google Container Registry.
Lastly it kicks off a deploy to Google Cloud Run.