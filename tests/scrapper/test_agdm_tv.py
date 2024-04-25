import pytest

from unittest.mock import Mock, patch
from anime_dl.object.episode import Episode
from anime_dl.scrapper.agdm_tv_creator import AgdmTvCreator
from anime_dl.scrapper.agdm_tv_scrapper import AgdmTvScrapper


@pytest.fixture()
def url():
    return {
        "episode": "https://agdm.tv/play/35480-1-1.html",
        "series": "https://agdm.tv/vod/35480.html",
    }


def test_creator():
    creator = AgdmTvCreator()
    scrapper = creator.factory_method()
    assert isinstance(scrapper, AgdmTvScrapper)


@pytest.fixture()
def scrapper():
    return AgdmTvScrapper()


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
                .set_series_name("SN")
                .set_season("na")
                .set_episode_name("EN")
                .set_episode_no("EN")
                .set_video_url("VU")
                .set_referer_url(url)
                .set_image_src("na")
            ), [],
        )
    )
    scrapper.test_connectivity = Mock(return_value=True)
    # test
    res = scrapper.get_episodes(url)
    assert len(res) == 1 and res[0].series_name == "SN" and res[0].video_url == "VU"


@pytest.mark.scrapping
def test_get_episodes_series(scrapper, url):
    url = url["series"]
    # given
    scrapper.parse_episode = Mock(
        return_value=(
            (
                Episode()
                .set_series_name("SN")
                .set_season("na")
                .set_episode_name("EN")
                .set_episode_no("EN")
                .set_video_url("VU")
                .set_referer_url(url)
                .set_image_src("na")
            ), [],
        )
    )
    scrapper.parse_series = Mock(
        return_value=[
            (
                Episode()
                .set_referer_url(url)
                .set_image_src("IS")
            )
        ]
    )
    scrapper.test_connectivity = Mock(return_value=True)
    # test
    res = scrapper.get_episodes(url)
    assert len(res) == 1 and res[0].video_url == "VU"
