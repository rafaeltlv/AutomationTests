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
        libgconf-2-4 \
        libnss3 \
        libasound2 \
        libatk-bridge2.0-0 \
        libgtk-3-0 \
        firefox \
        google-chrome-stable \
        microsoft-edge-dev \
    && wget -q -O - https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg && \
    install -o root -g root -m 644 microsoft.gpg /etc/apt/trusted.gpg.d/ && \
    sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/edge stable main" > /etc/apt/sources.list.d/microsoft-edge-dev.list' && \
    rm microsoft.gpg && \
    apt-get update && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY test_main.py /app/