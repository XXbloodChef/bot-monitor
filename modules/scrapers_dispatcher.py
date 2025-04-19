from scrapers.vinted_scraper import scrape_vinted
from scrapers.leboncoin_scraper import scrape_leboncoin

def run_all_scrapers():
    all_items = []
    all_items.extend(scrape_vinted())
    all_items.extend(scrape_leboncoin())
    return all_items
