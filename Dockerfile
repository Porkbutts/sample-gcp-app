FROM python:3.7-alpine

RUN apk update && apk add --virtual build-dependencies \
  gcc musl-dev

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
