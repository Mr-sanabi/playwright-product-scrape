# Playwright Product Scrape Lab

A focused browser-automation lab for scraping JavaScript-rendered quote cards and exporting them to CSV.

> This is an intentionally small Playwright lab rather than a general-purpose crawler.

## Features

- headless browser by default, with optional headed mode;
- configurable URL, output path, and positive result limit;
- explicit page timeout and guaranteed browser cleanup;
- automatic creation of the output directory;
- isolated writer tests that do not require launching a browser.

## Setup and usage

```bash
python -m pip install -r requirements.txt
python -m playwright install chromium
python -m src.main --limit 5 --output data/quotes.csv
```

Show the browser window during a run:

```bash
python -m src.main --headed
```

## Tests

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

## Stack

Python 3.11+, Playwright, argparse, CSV, pytest.
