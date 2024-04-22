from anime_dl.scrapper.creator import Creator
from anime_dl.scrapper.scrapper import Scrapper
from anime_dl.scrapper.anime1_me_scrapper import Anime1MeScrapper


class Anime1MeCreator(Creator):
    def factory_method(self) -> Scrapper:
        return Anime1MeScrapper()
