from anime_dl.scrapper.creator import Creator
from anime_dl.scrapper.scrapper import Scrapper
from anime_dl.scrapper.agdm_tv_scrapper import AgdmTvScrapper


class AgdmTvCreator(Creator):
    def factory_method(self) -> Scrapper:
        return AgdmTvScrapper()
