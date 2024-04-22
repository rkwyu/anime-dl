from anime_dl.scrapper.creator import Creator
from anime_dl.scrapper.scrapper import Scrapper
from anime_dl.scrapper.yhdm_one_scrapper import YhdmOneScrapper


class YhdmOneCreator(Creator):
    def factory_method(self) -> Scrapper:
        return YhdmOneScrapper()
