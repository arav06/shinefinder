# ShineFinder

#### Simple web scraper which will help you find jobs

This will scrape job data such as job title, company, experience required, etc. from [Shine](https://shine.com)

Once it finishes scraping, it will save all the information in a file

## Setup

```txt
git clone https://github.com/arav06/shinefinder
cd shinefinder
python3 shinefinder.py -h
```

## Usage

You will need to provide the job you are looking for, your location preference and the number of web pages you wish to check

```md
python3 shinefinder.py -j engineer -p 1 -l Delhi
python3 shinefinder.py --job "marketing executive" --location Mumbai -p 3
```

***
