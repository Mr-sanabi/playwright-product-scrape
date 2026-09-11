# Playwright Scraping Lab

A Python 3.11+ learning project that scrapes JavaScript-rendered quotes into CSV. Despite the repository name, the current example collects quotes, not products.

## Run

```bash
python -m pip install -r requirements.txt
python -m playwright install chromium
python -m src.main --limit 5 --output data/quotes.csv
```

The default source is `https://quotes.toscrape.com/js/`. Add `--headed` to see the browser or `--url URL` to change the page.

Selectors are written for quote cards; changing the URL does not make this a general-purpose scraper. Tests cover the writer without launching a browser.

## Tests

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
```
