FROM ubuntu:latest

ENV LANG="C.UTF-8"
ENV LC_ALL="C.UTF-8"
ENV PATH="${HOME}/.local/bin:$PATH"
ENV PIPENV_RUN_SYSTEM=1
ENV PIPENV_TIMEOUT=500

COPY . /opt
WORKDIR /opt

RUN apt-get update -y && apt-get upgrade -y &&\
    apt-get install -y git python3-pip python3-openssl &&\
    pip3 install pipenv --upgrade &&\
    pipenv install --three --dev &&\
    pipenv run test