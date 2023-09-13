# ivoox-scraping
Scrapes the [ivoox](https://www.ivoox.com/) website to download the podcast episode provided.

## Prerequisites

- [Python 3.10.x](https://www.python.org/downloads/)
- [Chrome browser](https://www.google.com/chrome/)

## Installation
### Chromedriver

Chromedriver file is automatically updated when running the script.

#### Manually installation

Install a compatible chromedirver version with your browser from https://chromedriver.chromium.org/downloads in 'chromedriver' folder in root project directory

### Requirements

`pip3 install -r requirements.txt`

## Using ivoox-scraping

Download specific podcast episode

`python3 main.py -p <podcast_key> -c '<Episode name or partial episode name>'`

Download the latest episode of specific podcast

`python3 main.py -p <podcast_key>`

## Configuration file

To add new podcast url you only need to modify config file (config.ini). Under `[PODCAST_URL]` section.

`<podcast_key> = '<podcast_url>'`

## Running with Docker

You can build the Docker image by cloning this repository and running:

```bash
docker build . -t ivoox-scraping
```

There is also a [ready to use image](https://hub.docker.com/repository/docker/jonazpiazu/ivoox-scraping/general) that you can use.

To run it you can use the following command:

```bash
docker run -it --rm -v $(pwd)/config.ini:/app/config.ini -v <path_here>/downloaded_podcast_audio:/app/downloaded_podcast_audio ivoox-scraping -p <podcast_key> -latest
```
