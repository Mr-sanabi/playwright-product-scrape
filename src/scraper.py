from playwright.sync_api import sync_playwright

def scrape_quotes(URL):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        page = browser.new_page()
        result = []

        page.goto(URL)
        quotes = page.locator(".quote")
        quotes.first.wait_for()
        count = quotes.count()
        
        for i in range(min(count, 5)):
            card = quotes.nth(i)
            quote_text = card.locator(".text").inner_text()
            author = card.locator(".author").inner_text()
            print(f"{quote_text} - {author}")
            result.append({
                "quote": quote_text,
                "author": author,
                "source_url": URL
                })
            