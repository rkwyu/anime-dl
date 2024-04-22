import pytest
from anime_dl.object.episode import Episode
from anime_dl.validator.season_validator import SeasonValidator


@pytest.fixture()
def validator():
    return SeasonValidator()


@pytest.mark.validation
def test_validate(validator):
    validator.validate(Episode().set_season("FOO"))


@pytest.mark.validation
def test_validate_empty(validator):
    with pytest.raises(Exception) as e_info:
        validator.validate(Episode())
