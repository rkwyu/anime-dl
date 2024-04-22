from unittest.mock import patch
import pytest
from anime_dl import anime_dl
from anime_dl.downloader.ffmpeg_strategy import FfmpegStrategy
from anime_dl.object.episode import Episode
from anime_dl.scrapper.creator import Creator


@patch.object(Creator, "get_episodes")
@patch.object(FfmpegStrategy, "download")
def test(mock1, mock2):
    assert FfmpegStrategy.download is mock1
    assert Creator.get_episodes is mock2
    mock2.return_value = [
        (
            Episode()
            .set_series_name("SN")
            .set_season("S")
            .set_episode_name("EN")
            .set_episode_no("EN")
            .set_video_url("VU.mp4")
            .set_referer_url("RU")
            .set_image_src("IS")
        )
    ]
    mock1.return_value = None
    anime_dl.main("https://anime1.in/FOO")
    anime_dl.main("https://anime1.me/FOO")
    anime_dl.main("https://www.xgcartoon.com/FOO")
    anime_dl.main("https://yhdm.one/FOO")


def test_main_empty():
    with pytest.raises(Exception) as e_info:
        anime_dl.main("")
