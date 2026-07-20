from playwright.sync_api import sync_playwright

def scrape_quotes(url, limit=5, headed=False):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=not headed)
        page = browser.new_page()
        result = []

        page.goto(url, wait_until="domcontentloaded", timeout=30_000)
        quotes = page.locator(".quote")
        quotes.first.wait_for()
        count = quotes.count()
        
        for i in range(min(count, limit)):
            card = quotes.nth(i)
            quote_text = card.locator(".text").inner_text()
            author = card.locator(".author").inner_text()
            print(f"{quote_text} - {author}")
            result.append({
                "quote": quote_text,
                "author": author,
                "source_url": url
                })
        browser.close()
        return result
