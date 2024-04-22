import pytest
from anime_dl.object.episode import Episode
from anime_dl.validator.series_name_validator import SeriesNameValidator


@pytest.fixture()
def validator():
    return SeriesNameValidator()


@pytest.mark.validation
def test_validate(validator):
    validator.validate(Episode().set_series_name("FOO"))


@pytest.mark.validation
def test_validate_empty(validator):
    with pytest.raises(Exception) as e_info:
        validator.validate(Episode())
