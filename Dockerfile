FROM python:3.7-alpine

RUN apk update && apk add --virtual build-dependencies \
  gcc musl-dev

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
