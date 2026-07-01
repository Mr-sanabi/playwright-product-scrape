# Playwright Product Scraper

Small Python scraping lab built with Playwright.

This project demonstrates browser-based scraping with Playwright instead of requests. It opens a JavaScript-rendered page, waits for rendered content, extracts data from the browser DOM, and saves the result to a CSV file.

Current version scrapes quotes from a JavaScript-rendered test page. It does not scrape real product pages or product catalogs yet. The project name is kept as a direction for the next step: applying the same Playwright patterns to dynamic product pages, catalogs, infinite scroll pages, and client-style data extraction tasks.

## Features

- Browser-based scraping with Playwright
- Works with JavaScript-rendered pages
- Extracts rendered page data through the browser DOM
- Uses Playwright locators
- Saves extracted records to CSV
- Modular project structure
- No requests-based page loading
- First step toward dynamic product and catalog scraping

## Tech Stack

- Python
- Playwright
- CSV
- PowerShell / CLI

## Project Structure

    playwright-product-scraper/
      src/
        main.py
        scraper.py
        writer.py

      data/
        .gitkeep

      README.md
      requirements.txt
      .gitignore

## Installation

Create and activate a virtual environment:

    python -m venv .venv
    .\.venv\Scripts\Activate.ps1

Install dependencies:

    pip install -r requirements.txt
    playwright install

## Usage

Run the scraper:

    python src/main.py

The script extracts quote records from a JavaScript-rendered page and saves the output to:

    data/quotes.csv

## Current Target

Current scraping target:

    https://quotes.toscrape.com/js/

This page is useful for a first Playwright lab because the content is rendered through JavaScript. The goal is to practice opening a real browser, waiting for rendered elements, selecting DOM nodes with locators, and extracting visible text.

## Output Fields

The generated CSV contains:

    quote
    author
    source_url

## Example Output

    quote,author,source_url
    "The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.",Albert Einstein,https://quotes.toscrape.com/js/
    "It is our choices, Harry, that show what we truly are, far more than our abilities.",J.K. Rowling,https://quotes.toscrape.com/js/

## What I Practiced

- Setting up Playwright in a Python project
- Opening browser pages programmatically
- Using Chromium through Playwright
- Working with page, locator, and nested locators
- Waiting for JavaScript-rendered elements
- Extracting visible text from the rendered DOM
- Saving browser-extracted data to CSV
- Splitting scraper logic into separate modules

## Limitations

This version does not scrape real products yet.

It currently extracts quotes from a JavaScript-rendered practice page. Product cards, prices, pagination, filters, lazy loading, infinite scroll, and real catalog extraction are planned as future improvements.

## Next Steps

Possible next improvements:

- Replace the quote target with a real product/catalog page
- Extract product title, price, availability, and product URL
- Add CLI arguments for input URL, output file, and record limit
- Add support for pagination or infinite scroll
- Add error handling for missing fields
- Add screenshots or debugging mode
- Turn this into a stronger portfolio scraper for dynamic websites

## Notes

This is a first Playwright scraping lab. The main goal is to understand browser-based scraping patterns before applying Playwright to more complex product pages, dynamic catalogs, infinite scroll pages, and client-style data extraction projects.