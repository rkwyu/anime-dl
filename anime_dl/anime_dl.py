import traceback
from urllib.parse import unquote
from anime_dl.const import regex
from anime_dl.downloader.downloader import Downloader
from anime_dl.downloader.ffmpeg_strategy import FfmpegStrategy
from anime_dl.scrapper.agdm_tv_creator import AgdmTvCreator
from anime_dl.scrapper.anime1_in_creator import Anime1InCreator
from anime_dl.scrapper.anime1_me_creator import Anime1MeCreator
from anime_dl.scrapper.xgcartoon_creator import XgCartoonCreator
from anime_dl.scrapper.yhdm_one_creator import YhdmOneCreator
from anime_dl.utils.logger import Logger
from anime_dl.validator.episode_name_validator import EpisodeNameValidator
from anime_dl.validator.season_validator import SeasonValidator
from anime_dl.validator.series_name_validator import SeriesNameValidator
from anime_dl.validator.video_url_validator import VideoUrlValidator
import re

logger = Logger()

# Map friendly names to creator classes
EXTRACTORS = {
    "xgcartoon.com": XgCartoonCreator,
    "lincartoon.com": XgCartoonCreator,
    "anime1.me": Anime1MeCreator,
    "anime1.in": Anime1InCreator,
    "yhdm.one": YhdmOneCreator,
    "agdm.tv": AgdmTvCreator,
}

def main(url: str) -> None:
    try:
        url = unquote(url)

        if re.search(regex.URL["lincartoon.com"]["domain"], url):
            url = url.replace("lincartoon.com", "xgcartoon.com")

        scrapper = None
        for name, creator_class in EXTRACTORS.items():
            if re.search(regex.URL[name.lower()]["domain"], url):
                scrapper = creator_class()
                break
            
        if scrapper is None:
            raise Exception(f"Unsupported URL: {url}")

        # scrapping
        episodes = scrapper.get_episodes(url)

        # validator
        video_url_validator = VideoUrlValidator()
        series_name_validator = SeriesNameValidator()
        season_validator = SeasonValidator()
        episode_name_validator = EpisodeNameValidator()
        video_url_validator.set_next(series_name_validator).set_next(
            season_validator
        ).set_next(episode_name_validator)

        # downloader
        ffmpeg_strategy = FfmpegStrategy()
        downloader = Downloader(ffmpeg_strategy)
        for episode in episodes:
            video_url_validator.validate(episode)
            downloader.download(episode)
    except Exception as e:
        logger.error(traceback.format_exc())
        raise e
    
def list_extractors() -> list[str]:
    return list(EXTRACTORS.keys())