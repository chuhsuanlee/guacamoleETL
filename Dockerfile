FROM python:3.5

WORKDIR /usr/src

ENTRYPOINT ["python", "test.py"]
