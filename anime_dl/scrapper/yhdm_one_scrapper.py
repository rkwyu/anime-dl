import json
import logging
import re
import requests
import typing

from anime_dl.const import regex, general
from anime_dl.object.episode import Episode
from anime_dl.scrapper.scrapper import Scrapper
from anime_dl.utils.logger import Logger
from anime_dl.utils.progress_bar import ProgressBar
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs

logger = Logger()


class YhdmOneScrapper(Scrapper):
    def get_episodes(self, url: str) -> typing.List[Episode]:
        if re.search(regex.URL["yhdm.one"]["series"], url):
            episodes = self.parse_series(url)
            progress_bar = ProgressBar("Link Fetching", 1, len(episodes))
            for episode in episodes:
                episode = episode.set_video_url(
                    self.parse_episode(episode.referer_url)[0].video_url
                )
                progress_bar.print()
            return episodes
        elif re.search(regex.URL["yhdm.one"]["episode"], url):
            episode, series_url = self.parse_episode(url)
            series = list(
                filter(
                    lambda i: i.referer_url == url,
                    self.parse_series(series_url),
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

    def parse_series(self, url: str) -> typing.List[Episode]:
        try:
            episodes = []
            headers = general.REQUEST["header"]
            doc = BeautifulSoup(requests.get(url, headers=headers).text, "html.parser")
            series_name = doc.select_one("h1.names").text.strip()
            image_src = doc.select_one("div.detail-poster img").attrs["src"].strip()
            episode_no = 1
            items = doc.select("div.ep-panel a")
            progress_bar = ProgressBar("Link Fetching", 1, len(episodes))
            for item in reversed(items):
                episode_name = item.text.strip()
                referer_url = "https://yhdm.one" + item.attrs["href"].strip()
                episodes.append(
                    Episode()
                    .set_series_name(series_name)
                    .set_season("na")
                    .set_episode_name(episode_name)
                    .set_episode_no(episode_no)
                    .set_referer_url(referer_url)
                    .set_image_src(image_src)
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
            series_url = "https://yhdm.one" + doc.select_one("h1 > a").attrs["href"].strip()
            episode_name = doc.select_one("h1 > a").text.strip() + doc.select_one("h1 > small").text.strip()
            m = re.search(regex.URL["yhdm.one"]["episode"], url)
            id = m.groups()[0]
            ep = m.groups()[1]
            resp = json.loads(requests.get(f"https://yhdm.one/_get_plays/{id}/{ep}", headers=headers).text)
            video_url = resp["video_plays"][0]["play_data"]
            return (
                Episode()
                .set_episode_name(episode_name)
                .set_video_url(video_url)
                .set_referer_url(url)
            ), series_url
        except Exception as e:
            logger.error(f"{url}: {e}")
            return Episode()
