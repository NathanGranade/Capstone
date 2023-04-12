FROM python:3.11

# set working directory
WORKDIR /usr/src/clab-app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean

# add and install requirements
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# add app
COPY . .
