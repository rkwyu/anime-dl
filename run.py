import argparse

from anime_dl import anime_dl
from anime_dl.utils.logger import Logger

logger = Logger()

parser = argparse.ArgumentParser()
parser.add_argument("url")
args = parser.parse_args()
if __name__ == "__main__":
    try:
        anime_dl.main(args.url)
    except Exception as e:
        logger.error(e)
