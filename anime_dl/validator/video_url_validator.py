from pydantic import ValidationError
from anime_dl.object.episode import Episode
from anime_dl.validator.abstract_validator import AbstractValidator


class VideoUrlValidator(AbstractValidator):
    def validate(self, episode: Episode) -> None:
        video_url = episode.video_url
        if video_url is None or (
            not video_url.endswith(".m3u8") and not video_url.endswith(".mp4")
        ):
            raise Exception(f"not .m3u8 / .mp4: {video_url}")
        else:
            return super().validate(episode)
