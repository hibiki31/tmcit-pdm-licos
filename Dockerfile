FROM python:3.8.6-buster

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install requests=2.25.0