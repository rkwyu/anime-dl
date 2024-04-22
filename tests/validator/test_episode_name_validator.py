import pytest
from anime_dl.object.episode import Episode
from anime_dl.validator.episode_name_validator import EpisodeNameValidator


@pytest.fixture()
def validator():
    return EpisodeNameValidator()


@pytest.mark.validation
def test_validate(validator):
    validator.validate(Episode().set_episode_name("FOO"))


@pytest.mark.validation
def test_validate_empty(validator):
    with pytest.raises(Exception) as e_info:
        validator.validate(Episode())
