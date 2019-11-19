FROM registry.lain.ein.plus/einplus/centos-base:20190925-slim

ADD . /lain/app
WORKDIR /lain/app
RUN pip install -r requirements.txt
