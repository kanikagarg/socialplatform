FROM ubuntu:20.04
FROM python:3.8

RUN apt-get update
RUN apt-get install -y unixodbc-dev
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
# EXPOSE 8000
# EXPOSE 443
WORKDIR /app/letsconnect
CMD bash run.sh
