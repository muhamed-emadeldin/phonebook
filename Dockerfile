
FROM python:3.9.6-slim-bullseye

WORKDIR /app/

COPY . /app/

RUN apt-get update && apt-get install -y inetutils-ping \
    && mkdir -p /tmp/slack_bot/mysqld && chmod -R 777 /tmp/slack_bot/mysqld \
    && apt-get -y install libxml2-dev libxslt-dev python-dev \
    && apt-get -y install python3-dev default-libmysqlclient-dev build-essential \
    && python -m pip install --upgrade setuptools \
    && apt-get -y install graphviz graphviz-dev \
    && python -m venv /opt/proj_env \
    && python -m pip install --upgrade pip \
    && /opt/proj_env/bin/pip install -r /app/requirements.txt \
    && chmod +x /app/entrypoint.sh

ENV PIP_ROOT_USER_ACTION=ignore
ENV VIRTUAL_ENV=/opt/proj_env
ENV PATH="/opt/proj_env/bin:$PATH"
