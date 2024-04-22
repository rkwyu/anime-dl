import pytest

from unittest.mock import Mock, patch
from anime_dl.object.episode import Episode
from anime_dl.scrapper.xgcartoon_creator import XgCartoonCreator
from anime_dl.scrapper.xgcartoon_scrapper import XgCartoonScrapper


@pytest.fixture()
def url():
    return {
        "episode": "https://www.xgcartoon.com/video/labixiaowangguomenghuanlabiwangguoyueyu-fuyonglingsan/uK7R3uqhqt.html",
        "series": "https://www.xgcartoon.com/detail/labixiaowangguomenghuanlabiwangguoyueyu-fuyonglingsan",
    }


def test_creator():
    creator = XgCartoonCreator()
    scrapper = creator.factory_method()
    assert isinstance(scrapper, XgCartoonScrapper)


@pytest.fixture()
def scrapper():
    return XgCartoonScrapper()


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
            Episode().set_episode_name("EN").set_video_url("VU").set_referer_url(url)
        )
    )
    scrapper.parse_series = Mock(
        return_value=[
            (
                Episode()
                .set_series_name("SN")
                .set_season("S")
                .set_episode_name("EN")
                .set_episode_no("EN")
                .set_referer_url(url)
                .set_image_src("IS")
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
    scrapper.parse_episode = Mock(
        return_value=(
            Episode().set_episode_name("EN").set_video_url("VU").set_referer_url(url)
        )
    )
    scrapper.parse_series = Mock(
        return_value=[
            (
                Episode()
                .set_series_name("SN")
                .set_season("S")
                .set_episode_name("EN")
                .set_episode_no("EN")
                .set_referer_url(url)
                .set_image_src("IS")
            )
        ]
    )
    # test
    res = scrapper.get_episodes(url)
    assert len(res) == 1 and res[0].video_url == "VU"
