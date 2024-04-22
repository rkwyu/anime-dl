from abc import ABC, abstractmethod

from anime_dl.object.episode import Episode


class Strategy(ABC):
    @abstractmethod
    def download(self, episode: Episode):
        pass
