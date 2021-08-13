from typing import Dict


class Scraper():
    """
    This is just an interface which should be implemented by each scraper class.
    """

    def getPrices(self, modelname: str) -> dict[str:float]:
        """
        Should return a dict which maps a model to the current price.
        """
        pass
