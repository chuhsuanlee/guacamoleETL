FROM python:3.5

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

## copy file to /usr/src/app
COPY ./improved-guacamole /usr/src/app

ENTRYPOINT ["python", "main.py"]
