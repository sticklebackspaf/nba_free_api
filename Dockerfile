# syntax=docker/dockerfile:1

FROM python:3.11.5-alpine

WORKDIR /BV_CHALLENGE

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_APP=app_nba_api.py

#included db creating from sql ddl statement
RUN apk --update-cache add sqlite bash
# RUN apk rm -rf /var/cache/apk/*
RUN bash ./db/create-database.sh 

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]