import logging

from anime_dl.utils.config_loader import ConfigLoader

config_loader = ConfigLoader()
logging.basicConfig(
    level=int(config_loader.get(section="LOGGING", key="level")),
    format="[%(asctime)s] %(name)s [%(levelname)-8s]: %(message)s",
)


class LoggerMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Logger(metaclass=LoggerMeta):
    def __init__(self) -> None:
        self.logger = logging.getLogger("ANIME-DL")

    def info(self, *messages) -> None:
        for message in messages:
            self.logger.info(message)

    def warning(self, *messages) -> None:
        for message in messages:
            self.logger.warning(message)

    def error(self, *messages) -> None:
        for message in messages:
            self.logger.error(message)
