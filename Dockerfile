FROM python:3.10-slim

WORKDIR /app

# Download and install Chrome browser
RUN apt-get update -qq \
    && apt-get install -qq -y wget unzip gpg \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /etc/apt/trusted.gpg.d/google-archive-keyring.gpg \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update -qq \
    && apt-get install -qq -y google-chrome-stable \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# This is needed for Chrome to work in the container
RUN apt-get update -qq && apt-get install -y xvfb \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN pip install pyvirtualdisplay

COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt

# Specify the command to run your application with arguments
ENTRYPOINT [ "python", "main.py" ]
