FROM python:3.11-slim-buster

ENV CGO_ENABLED=0

RUN set -ex \
    && curl -sL https://deb.nodesource.com/setup_14.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g typescript \
    && pip3 install pytest \
    && apt-get install -y \
        build-essential \
        gnupg2 \
        curl \
        wget \
        unzip \
        xvfb \
        x11vnc \
        fluxbox \
        xterm \
        libconfig-2-4 \
        libnss3 \
        libasound2 \
        libatk-bridge2.0-0 \
        libgtk-3-0 \
        google-chrome-stable \
    && apt-get update \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

    WORKDIR /app

    COPY test_main.py /app/