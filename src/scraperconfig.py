from src.scrapers.scraper import Scraper
from .scrapers.geizhals_scraper import GeizhalsScraper

scrapers: dict[str: Scraper] = {
    'geizhals': GeizhalsScraper()
}
