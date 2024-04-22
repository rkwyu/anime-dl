from anime_dl.scrapper.creator import Creator
from anime_dl.scrapper.scrapper import Scrapper
from anime_dl.scrapper.anime1_in_scrapper import Anime1InScrapper


class Anime1InCreator(Creator):
    def factory_method(self) -> Scrapper:
        return Anime1InScrapper()
