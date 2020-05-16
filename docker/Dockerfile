FROM ubuntu:18.04

RUN apt-get update && apt-get install --yes \
        build-essential \
        gcc \
        git \
        python3-pip \
        curl \
        musl-dev

RUN pip3 --no-cache-dir install -U pip
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash -
RUN apt-get install -y nodejs

COPY package*.json /npm_packages/
COPY binder/requirements.txt /python_binder_requirements/

RUN npm install -g gatsby-cli
RUN npm install /npm_packages/

RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 10
RUN update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 10

RUN pip install -r /python_binder_requirements/requirements.txt

WORKDIR /host
