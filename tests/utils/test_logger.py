from anime_dl.utils.logger import Logger


def test():
    logger = Logger()
    logger.info("INFO")
    logger.warning("WARN")
    logger.error("ERROR")
