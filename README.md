# ivoox-scraping
Scrapes the [ivoox](https://www.ivoox.com/) website to download the podcast episode provided.

## Prerequisites

- Python 3.10.x

## Installation
### Chromedriver

Install tou chromedirver version from https://chromedriver.chromium.org/downloads in 'chromedriver' folder in root project directory

### Requirements

`pip3 install -r requirements.txt`

## Using ivoox-scraping

`python3 main.py <podcast_key> '<Chapter name or partial chapter name>'`

## Configuration file

To add new podcast url you only need to modify config file (config.ini). Under `[PODCAST_URL]` section.

`<podcast_key> = '<podcast_url>'`