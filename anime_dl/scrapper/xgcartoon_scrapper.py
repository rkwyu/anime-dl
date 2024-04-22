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


class XgCartoonScrapper(Scrapper):
    def get_episodes(self, url: str) -> typing.List[Episode]:
        if re.search(regex.URL["xgcartoon"]["series"], url):
            m = re.search(regex.URL["xgcartoon"]["series"], url)
            cartoon_id = m.groups()[0]
            episodes = self.parse_series(url)
            progress_bar = ProgressBar("Link Fetching", 1, len(episodes))
            for episode in episodes:
                episode = episode.set_video_url(
                    self.parse_episode(episode.referer_url).video_url
                )
                progress_bar.print()
            return episodes
        elif re.search(regex.URL["xgcartoon"]["episode"], url):
            m = re.search(regex.URL["xgcartoon"]["episode"], url)
            cartoon_id = m.groups()[0]
            chapter_id = m.groups()[1]
            episode = self.parse_episode(url)
            series = list(
                filter(
                    lambda i: i.referer_url == url,
                    self.parse_series(f"https://www.xgcartoon.com/detail/{cartoon_id}"),
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
            series_name = doc.select_one("h1.h1").text.strip()
            image_src = doc.select_one(".detail-sider > amp-img").attrs["src"].strip()
            season = None
            episode_no = 1
            items = doc.select("div.detail-right__volumes > div.row > div")
            for item in items:
                if "volume-title" in item.attrs["class"]:
                    season = item.text.strip()
                    episode_no = 1
                else:
                    chapter = item.select_one("a.goto-chapter")
                    if chapter:
                        episode_name = chapter.attrs["title"].strip()
                        href = chapter.attrs["href"].strip()
                        cartoon_id = parse_qs(urlparse(href).query)["cartoon_id"][0]
                        chapter_id = parse_qs(urlparse(href).query)["chapter_id"][0]
                        referer_url = f"https://www.xgcartoon.com/video/{cartoon_id}/{chapter_id}.html"
                        episodes.append(
                            Episode()
                            .set_series_name(series_name)
                            .set_season(season)
                            .set_episode_name(episode_name)
                            .set_episode_no(episode_no)
                            .set_referer_url(referer_url)
                            .set_image_src(image_src)
                        )
                        episode_no = episode_no + 1
            return episodes
        except Exception as e:
            logger.error(f"{url}: {e}")
            return []

    def parse_episode(self, url: str) -> Episode:
        try:
            headers = general.REQUEST["header"]
            doc = BeautifulSoup(requests.get(url, headers=headers).text, "html.parser")
            episode_name = doc.select_one("h1.h1").text.strip()
            iframe_src = doc.select_one("iframe").attrs["src"].strip()
            if "vid" in parse_qs(urlparse(iframe_src).query):
                vid = parse_qs(urlparse(iframe_src).query)["vid"][0]
                video_url = f"https://xgct-video.vzcdn.net/{vid}/playlist.m3u8"
            else:
                video_url = self.parse_iframe(iframe_src)
            return (
                Episode()
                .set_episode_name(episode_name)
                .set_video_url(video_url)
                .set_referer_url(url)
            )
        except Exception as e:
            logger.error(f"{url}: {e}")
            return Episode()

    def parse_iframe(self, url: str) -> str:
        try:
            headers = general.REQUEST["header"]
            doc = BeautifulSoup(requests.get(url, headers=headers).text, "html.parser")
            return doc.select_one("video#main-video source").attrs["src"].strip()
        except Exception as e:
            logger.error(f"{url}: {e}")
            return Episode()
