from anime_dl.scrapper.creator import Creator
from anime_dl.scrapper.scrapper import Scrapper
from anime_dl.scrapper.xgcartoon_scrapper import XgCartoonScrapper


class XgCartoonCreator(Creator):
    def factory_method(self) -> Scrapper:
        return XgCartoonScrapper()
