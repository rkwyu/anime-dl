import json
import logging
import regex as re
import requests
import typing

from anime_dl.const import regex, general
from anime_dl.object.episode import Episode
from anime_dl.scrapper.scrapper import Scrapper
from anime_dl.utils.logger import Logger
from anime_dl.utils.progress_bar import ProgressBar
from bs4 import BeautifulSoup

logger = Logger()


class Anime1InScrapper(Scrapper):
    def get_episodes(self, url: str) -> typing.List[Episode]:
        if re.search(regex.URL["anime1.in"]["series"], url):
            if self.is_series(url):
                return self.parse_series(url)
            else:
                episode, series_url = self.parse_episode(url)
                series = list(
                    filter(
                        lambda i: i.episode_name == episode.episode_name,
                        self.get_info(series_url),
                    )
                )
                if len(series) == 1:
                    episode = (
                        episode.set_series_name(series[0].series_name)
                        .set_season(series[0].season)
                        .set_episode_no(series[0].episode_no)
                        .set_image_src(series[0].image_src)
                    )
                return [episode]
        else:
            raise Exception(f"Unsupported URL: {url}")

    def is_series(self, url: str) -> bool:
        try:
            headers = general.REQUEST["header"]
            doc = BeautifulSoup(requests.get(url, headers=headers).text, "html.parser")
            return doc.select_one("h1.page-title") is not None
        except Exception as e:
            logger.error(f"{url}: {e}")
            return []

    def get_info(self, url: str) -> typing.List[Episode]:
        try:
            episodes = []
            headers = general.REQUEST["header"]
            doc = BeautifulSoup(requests.get(url, headers=headers).text, "html.parser")
            series_name = doc.select_one("h1.page-title").text.strip()
            articles = doc.select("article")
            episode_no = 1
            for article in reversed(articles):
                episode_name = article.select_one("h2.entry-title").text.strip()
                episodes.append(
                    Episode()
                    .set_series_name(series_name)
                    .set_season("na")
                    .set_episode_name(episode_name)
                    .set_episode_no(episode_no)
                    .set_image_src("na")
                )
                episode_no = episode_no + 1
            return episodes
        except Exception as e:
            logger.error(f"{url}: {e}")
            return []

    def parse_series(self, url: str) -> typing.List[Episode]:
        try:
            episodes = []
            headers = general.REQUEST["header"]
            doc = BeautifulSoup(requests.get(url, headers=headers).text, "html.parser")
            series_name = doc.select_one("h1.page-title").text.strip()
            articles = doc.select("article")
            episode_no = 1
            progress_bar = ProgressBar("Link Fetching", 1, len(articles))
            for article in reversed(articles):
                episode_name = article.select_one("h2.entry-title").text.strip()
                referer_url = (
                    article.select_one("h2.entry-title a").attrs["href"].strip()
                )
                iframe_src = (
                    "https://anime1.in"
                    + article.select_one("iframe.vframe").attrs["src"].strip()
                )
                video_url = self.parse_iframe(iframe_src)
                episodes.append(
                    Episode()
                    .set_series_name(series_name)
                    .set_season("na")
                    .set_episode_name(episode_name)
                    .set_episode_no(episode_no)
                    .set_video_url(video_url)
                    .set_referer_url(referer_url)
                    .set_image_src("na")
                )
                episode_no = episode_no + 1
                progress_bar.print()
            return episodes
        except Exception as e:
            logger.error(f"{url}: {e}")
            return []

    def parse_episode(self, url: str) -> tuple[Episode, str]:
        try:
            headers = general.REQUEST["header"]
            doc = BeautifulSoup(requests.get(url, headers=headers).text, "html.parser")
            series_url = (
                "https://anime1.in/"
                + doc.select_one("p > a[href^='/']").attrs["href"].strip()
            )
            episode_name = doc.select_one("h1.entry-title").text.strip()
            iframe_src = (
                "https://anime1.in"
                + doc.select_one("iframe.vframe").attrs["src"].strip()
            )
            video_url = self.parse_iframe(iframe_src)
            return (
                Episode()
                .set_episode_name(episode_name)
                .set_video_url(video_url)
                .set_referer_url(url)
            ), series_url
        except Exception as e:
            logger.error(f"{url}: {e}")
            return Episode()

    def parse_iframe(self, url: str) -> str:
        try:
            headers = general.REQUEST["header"]
            doc = BeautifulSoup(requests.get(url, headers=headers).text, "html.parser")
            return doc.select_one("video source").attrs["src"].strip()
        except Exception as e:
            logger.error(f"{url}: {e}")
            return Episode()
