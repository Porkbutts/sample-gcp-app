FROM phusion/baseimage:latest

RUN apt-get update && apt-get install -y python-dev python-pip

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]