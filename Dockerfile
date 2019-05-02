FROM tukida/python-3.7
MAINTAINER kietnt17

COPY requirements.txt /
RUN mkdir -p /etc/uwsgi/ && mkdir -p /var/log/apps && pip --no-cache-dir install -r requirements.txt

COPY . /webapps/fptplay-api
WORKDIR /webapps/fptplay-api

EXPOSE 8080
