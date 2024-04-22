from pydantic import ValidationError
from anime_dl.object.episode import Episode
from anime_dl.validator.abstract_validator import AbstractValidator


class EpisodeNameValidator(AbstractValidator):
    def validate(self, episode: Episode) -> None:
        episode_name = episode.episode_name
        if episode_name is None:
            raise Exception(f"invalid episode_name: {episode_name}")
        else:
            return super().validate(episode)
