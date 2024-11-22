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
import os

logger = Logger()


def main(url: str) -> None:
    try:
        url = unquote(url)

        if re.search(regex.URL["lincartoon"]["domain"], url):
            url = url.replace("lincartoon.com", "xgcartoon.com")
        if re.search(regex.URL["dailygh"]["domain"], url):
            url = url.replace("dailygh.com", "xgcartoon.com")
        
        if re.search(regex.URL["xgcartoon"]["domain"], url):
            scrapper = XgCartoonCreator()
        elif re.search(regex.URL["anime1.me"]["domain"], url):
            scrapper = Anime1MeCreator()
        elif re.search(regex.URL["anime1.in"]["domain"], url):
            scrapper = Anime1InCreator()
        elif re.search(regex.URL["yhdm.one"]["domain"], url):
            scrapper = YhdmOneCreator()
        elif re.search(regex.URL["agdm.tv"]["domain"], url):
            scrapper = AgdmTvCreator()
        else:
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
            fn = episode.series_name+"."+episode.season+"."+episode.episode_name+".mp4"
            if fn in os.listdir("output"):
                print("Skip "+fn+" (downloaded)")
            else:
                video_url_validator.validate(episode)
                downloader.download(episode)
    except Exception as e:
        logger.error(traceback.format_exc())
        raise e
