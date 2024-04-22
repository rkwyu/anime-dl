import pytest

from unittest.mock import Mock, patch
from anime_dl.object.episode import Episode
from anime_dl.scrapper.anime1_me_creator import Anime1MeCreator
from anime_dl.scrapper.anime1_me_scrapper import Anime1MeScrapper


@pytest.fixture()
def url():
    return {
        "episode": "https://anime1.me/22813",
        "series": "https://anime1.me/category/2023年冬季/魔王學院的不適任者-第二季",
    }


def test_creator():
    creator = Anime1MeCreator()
    scrapper = creator.factory_method()
    assert isinstance(scrapper, Anime1MeScrapper)


@pytest.fixture()
def scrapper():
    return Anime1MeScrapper()


@pytest.mark.scrapping
def test_get_episodes_empty(scrapper):
    with pytest.raises(Exception) as e_info:
        scrapper.get_episodes("")


@pytest.mark.scrapping
def test_get_episodes_episode(scrapper, url):
    url = url["episode"]
    # given
    scrapper.parse_episode = Mock(
        return_value=(
            (
                Episode()
                .set_episode_name("EN")
                .set_video_url("VU")
                .set_referer_url(url)
            ),
            "SU",
        )
    )
    scrapper.get_info = Mock(
        return_value=[
            (
                Episode()
                .set_series_name("SN")
                .set_season("na")
                .set_episode_name("EN")
                .set_episode_no("EN")
                .set_image_src("na")
            )
        ]
    )
    # test
    res = scrapper.get_episodes(url)
    assert len(res) == 1 and res[0].series_name == "SN" and res[0].video_url == "VU"


@pytest.mark.scrapping
def test_get_episodes_series(scrapper, url):
    url = url["series"]
    # given
    scrapper.parse_series = Mock(
        return_value=[
            (
                Episode()
                .set_series_name("SN")
                .set_season("na")
                .set_episode_name("EN")
                .set_episode_no("EN")
                .set_video_url("VU")
                .set_referer_url(url)
                .set_image_src("na")
            )
        ]
    )
    # test
    res = scrapper.get_episodes(url)
    assert len(res) == 1 and res[0].video_url == "VU"
