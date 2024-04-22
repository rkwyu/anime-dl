from abc import ABC, abstractmethod


class Scrapper(ABC):
    @abstractmethod
    def get_episodes(self, url: str):
        pass
