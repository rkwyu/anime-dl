import json


class Episode:
    def __init__(self) -> None:
        self.series_name = None
        self.season = None
        self.episode_name = None
        self.episode_no = None
        self.video_url = None
        self.referer_url = None
        self.image_src = None

    def set_series_name(self, series_name: str) -> "Episode":
        self.series_name = series_name
        return self

    def set_season(self, season: str) -> "Episode":
        self.season = season
        return self

    def set_episode_name(self, episode_name: str) -> "Episode":
        self.episode_name = episode_name
        return self

    def set_episode_no(self, episode_no: str) -> "Episode":
        self.episode_no = episode_no
        return self

    def set_video_url(self, video_url: str) -> "Episode":
        self.video_url = video_url
        return self

    def set_referer_url(self, referer_url: str) -> "Episode":
        self.referer_url = referer_url
        return self

    def set_image_src(self, image_src: str) -> "Episode":
        self.image_src = image_src
        return self

    def __str__(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__)

    def __repr__(self) -> str:
        return self.__str__()
