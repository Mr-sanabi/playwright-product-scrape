from writer import save_csv
from scraper import scrape_quotes

def main():
    URL = "https://quotes.toscrape.com/js/"

    
    result = scrape_quotes(URL)
    save_csv("data/quotes.csv", result)


if __name__ == "__main__":
    main()