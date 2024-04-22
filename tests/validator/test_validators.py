from anime_dl.object.episode import Episode
from anime_dl.validator.episode_name_validator import EpisodeNameValidator
from anime_dl.validator.season_validator import SeasonValidator
from anime_dl.validator.series_name_validator import SeriesNameValidator
from anime_dl.validator.video_url_validator import VideoUrlValidator


def test():
    video_url_validator = VideoUrlValidator()
    series_name_validator = SeriesNameValidator()
    season_validator = SeasonValidator()
    episode_name_validator = EpisodeNameValidator()
    video_url_validator.set_next(series_name_validator).set_next(
        season_validator
    ).set_next(episode_name_validator)
    video_url_validator.validate(
        Episode()
        .set_video_url("FOO.mp4")
        .set_series_name("BAR")
        .set_season("BAZ")
        .set_episode_name("QUX")
    )
