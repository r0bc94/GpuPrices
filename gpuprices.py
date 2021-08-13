from src import scrapers
import urllib
from bs4 import BeautifulSoup

from src.scraperconfig import scrapers
print(scrapers)

for source, scraper in scrapers.items():
    print(f'source: {source}\tprices: {scraper.getPrices("3080ti")}')
