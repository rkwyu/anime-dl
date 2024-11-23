import traceback
import ffmpeg
import os

from pathvalidate import sanitize_filename
from anime_dl.downloader.strategy import Strategy
from anime_dl.object.episode import Episode
from anime_dl.utils.config_loader import ConfigLoader
from anime_dl.utils.logger import Logger

logger = Logger()
config_loader = ConfigLoader()


class FfmpegStrategy(Strategy):
    def download(self, episode: Episode) -> None:
        try:
            url = episode.video_url
            filename = (
                f"{episode.series_name}.{episode.season}.{episode.episode_name}.mp4"
            )
            fnt = f"{episode.series_name}.{episode.season}.{episode.episode_name}_temp.mp4"
            output = os.path.join(
                config_loader.get(section="DIRECTORY", key="output"),
                sanitize_filename(filename),
            )
            output_t = os.path.join(
                config_loader.get(section="DIRECTORY", key="output"),
                sanitize_filename(fnt),
            )
            os.makedirs(os.path.dirname(output), exist_ok=True)
            logger.info(f"started download: {filename} ({url})")
            stream = ffmpeg.input(url)
            stream = ffmpeg.output(stream, output_t, vcodec="copy", acodec="copy")
            ffmpeg.run(stream)
            os.rename(output_t,output)
            logger.info(f"downloaded: {filename}")
        except:
            logger.error(traceback.format_exc())
