from anime_dl.downloader.strategy import Strategy


class Downloader:
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def download(self, data: dict) -> bool:
        result = self._strategy.download(data)
