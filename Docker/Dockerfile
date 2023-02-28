FROM python:3.11-slim-buster

ENV CGO_ENABLED=0

# Install system packages and tools
RUN apt-get update && \
    apt-get install -y gnupg2 \
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
    build-essential

# Install Chrome, Firefox, and Edge browsers
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && apt-get install -y google-chrome-stable
RUN apt-get install -y firefox
RUN wget -q -O - https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg && \
    install -o root -g root -m 644 microsoft.gpg /etc/apt/trusted.gpg.d/ && \
    sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/edge stable main" > /etc/apt/sources.list.d/microsoft-edge-dev.list' && \
    rm microsoft.gpg && \
    apt-get update && apt-get install -y microsoft-edge-dev

# Install Node.js and TypeScript
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g typescript

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["pytest", "test_main.py"]
