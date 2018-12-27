FROM ubuntu:bionic

LABEL Name=nearby_shops Version=0.0.1
EXPOSE 8000

RUN apt-get update
RUN apt-get install -y aptitude
RUN aptitude install -y \
    binutils \
    gdal-bin \
    libgdal-dev \
    libproj-dev \
    postgresql-client \
    python3-dev \
    python3-gdal \
    python3-pip

WORKDIR /app
ENV PYTHONPATH "${PYTHONPATH}:/app"

ADD requirements.txt .
RUN pip3 install -r requirements.txt

ADD . /app
