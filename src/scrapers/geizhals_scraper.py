import urllib.request
from bs4 import BeautifulSoup

from .scraper import Scraper

class GeizhalsScraper(Scraper):
    """
    This is an implementation for the Geizhals Scraper, which looks for the average
    prices on Geizhalz for multiple models.
    """

    def getPrices(self, modelname: str) -> dict[str:float]:
        html = self.__getHtml(modelname)
        return self.__scrapePrices(html)

    def __getHtml(self, modelname):
        url = f'https://geizhals.de/?fs=rtx%203080ti&hloc=at&hloc=de&cat=gra16_512'

        req = urllib.request.Request(
            url, 
            data=None, 
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
            }
        )

        with urllib.request.urlopen(req) as response:
            html = response.read()
            return html


    def __scrapePrices(self, html: str) -> dict[str:float]:
        outdict = {}
        soup = BeautifulSoup(html, 'html.parser')
        # print(soup)
        
        listentries = soup.find_all('div', {'class': 'listview__content'})
        for listentry in listentries:

            variant = listentry.findAll('span', {'class': 'listview__label--variant'})
            if len(variant) == 0:
                # Ignoring the different models, just search for the vendors 
                continue

            nametag = listentry.findAll('a', {'class': 'listview__name-link'})
            name = nametag[0].text.strip()

            pricetag = listentry.findAll('span', {'class': 'price'})
            price = pricetag[0].text.strip().split(' ')[1].replace(',','.')

            outdict[name] = float(price)

        return outdict
