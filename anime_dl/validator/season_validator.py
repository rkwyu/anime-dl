from pydantic import ValidationError
from anime_dl.object.episode import Episode
from anime_dl.validator.abstract_validator import AbstractValidator


class SeasonValidator(AbstractValidator):
    def validate(self, episode: Episode) -> None:
        season = episode.season
        if season is None:
            raise Exception(f"invalid season: {season}")
        else:
            return super().validate(episode)
