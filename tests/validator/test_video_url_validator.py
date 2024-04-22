import pytest
from anime_dl.object.episode import Episode
from anime_dl.validator.season_validator import SeasonValidator
from anime_dl.validator.video_url_validator import VideoUrlValidator


@pytest.fixture()
def validator():
    return VideoUrlValidator()


@pytest.mark.validation
def test_validate_m3u8(validator):
    validator.validate(Episode().set_video_url("FOO.m3u8"))


@pytest.mark.validation
def test_validate_mp3(validator):
    validator.validate(Episode().set_video_url("FOO.mp4"))


@pytest.mark.validation
def test_validate_empty(validator):
    with pytest.raises(Exception) as e_info:
        validator.validate(Episode())


@pytest.mark.validation
def test_validate_invalid(validator):
    with pytest.raises(Exception) as e_info:
        validator.validate(Episode().set_video_url("FOO"))
