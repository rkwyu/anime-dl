import pytest

from unittest.mock import Mock, patch
from anime_dl.object.episode import Episode
from anime_dl.scrapper.yhdm_one_creator import YhdmOneCreator
from anime_dl.scrapper.yhdm_one_scrapper import YhdmOneScrapper


@pytest.fixture()
def url():
    return {
        "episode": "https://yhdm.one/vod-play/2024579756/ep4.html",
        "series": "https://yhdm.one/vod/2024579756.html",
    }


def test_creator():
    creator = YhdmOneCreator()
    scrapper = creator.factory_method()
    assert isinstance(scrapper, YhdmOneScrapper)


@pytest.fixture()
def scrapper():
    return YhdmOneScrapper()


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
            (Episode().set_episode_name("EN").set_video_url("VU").set_referer_url(url)),
            "SU",
        )
    )
    scrapper.parse_series = Mock(
        return_value=[
            (
                Episode()
                .set_series_name("SN")
                .set_season("na")
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
            (Episode().set_episode_name("EN").set_video_url("VU").set_referer_url(url)),
            "SU",
        )
    )
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
