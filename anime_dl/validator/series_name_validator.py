from pydantic import ValidationError
from anime_dl.object.episode import Episode
from anime_dl.validator.abstract_validator import AbstractValidator


class SeriesNameValidator(AbstractValidator):
    def validate(self, episode: Episode) -> None:
        series_name = episode.series_name
        if series_name is None:
            raise Exception(f"invalid series_name: {series_name}")
        else:
            return super().validate(episode)
