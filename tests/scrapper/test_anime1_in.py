import pytest

from unittest.mock import Mock, patch
from anime_dl.object.episode import Episode
from anime_dl.scrapper.anime1_in_creator import Anime1InCreator
from anime_dl.scrapper.anime1_in_scrapper import Anime1InScrapper


@pytest.fixture()
def url():
    return {
        "episode": "https://anime1.in/2024-mo-wang-xue-yuan-de-bu-shi-ren-zhe-di-er-ji-hou-ban-pian-10002000",
        "series": "https://anime1.in/2024-mo-wang-xue-yuan-de-bu-shi-ren-zhe-di-er-ji-hou-ban-pian/",
    }


def test_creator():
    creator = Anime1InCreator()
    scrapper = creator.factory_method()
    assert isinstance(scrapper, Anime1InScrapper)


@pytest.fixture()
def scrapper():
    return Anime1InScrapper()


@pytest.mark.scrapping
def test_get_episodes_empty(scrapper):
    with pytest.raises(Exception) as e_info:
        scrapper.get_episodes("")


@pytest.mark.scrapping
def test_get_episodes_episode(scrapper, url):
    url = url["episode"]
    # given
    scrapper.is_series = Mock(return_value=False)
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
    scrapper.is_series = Mock(return_value=True)
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
