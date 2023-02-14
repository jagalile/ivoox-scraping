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
