FROM python:3.5

RUN mkdir -p /usr/src/guacamoleETL
WORKDIR /usr/src/guacamoleETL
COPY ./guacamoleETL /usr/src/guacamoleETL

WORKDIR /usr/src
COPY test.py /usr/src/

ENTRYPOINT ["python", "test.py"]
