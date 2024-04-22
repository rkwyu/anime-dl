import configparser
import os


config = configparser.ConfigParser()
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))  # ../../
config.read(os.path.join(ROOT_DIR, "config.ini"))


class ConfigLoaderMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class ConfigLoader(metaclass=ConfigLoaderMeta):
    def get(self, section: str, key: str) -> str:
        return config[section][key]
