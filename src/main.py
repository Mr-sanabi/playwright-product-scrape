import argparse

from src.scraper import scrape_quotes
from src.writer import save_csv


def positive_int(value):
    number = int(value)
    if number < 1:
        raise argparse.ArgumentTypeError("limit must be a positive integer")
    return number


def parse_args():
    parser = argparse.ArgumentParser(description="Scrape JavaScript-rendered quotes with Playwright.")
    parser.add_argument("--url", default="https://quotes.toscrape.com/js/", help="Page to scrape")
    parser.add_argument("--output", default="data/quotes.csv", help="CSV output path")
    parser.add_argument("--limit", type=positive_int, default=5, help="Maximum number of quotes")
    parser.add_argument("--headed", action="store_true", help="Show the browser window")
    return parser.parse_args()


def main():
    args = parse_args()
    rows = scrape_quotes(args.url, args.limit, args.headed)
    save_csv(args.output, rows)


if __name__ == "__main__":
    main()
