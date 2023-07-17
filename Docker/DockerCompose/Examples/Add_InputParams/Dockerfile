FROM python:3.10.12-slim-bullseye

RUN apt-get update

COPY . .

RUN pip3 install --upgrade pip && pip3 install --no-cache-dir -r requirements.txt
