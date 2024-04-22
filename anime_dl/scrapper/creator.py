import typing

from abc import ABC, abstractmethod
from anime_dl.object.episode import Episode


class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def get_episodes(self, url: str) -> typing.List[Episode]:
        scrapper = self.factory_method()
        # TODO: pending logic
        return scrapper.get_episodes(url)
