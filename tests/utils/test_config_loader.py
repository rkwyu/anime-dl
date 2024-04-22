import pytest
from anime_dl.utils.config_loader import ConfigLoader


@pytest.mark.data_loading
def test_get():
    config_loader = ConfigLoader()
    value = config_loader.get("DIRECTORY", "OUTPUT")
    assert isinstance(value, str)


@pytest.mark.data_loading
def test_get_invalid_section():
    with pytest.raises(KeyError) as e_info:
        config_loader = ConfigLoader()
        config_loader.get("DIRECTORY", "FOO")


@pytest.mark.data_loading
def test_get_invalid_key():
    with pytest.raises(KeyError) as e_info:
        config_loader = ConfigLoader()
        config_loader.get("FOO", "BAR")
