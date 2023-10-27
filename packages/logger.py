import logging


def setup_logger(log_level=logging.INFO):
    logger = logging.getLogger("API")
    logger.setLevel(log_level)
    ch = logging.StreamHandler()
    formatter = logging.Formatter(
        "\033[93m%(levelname)s:\t%(filename)s: \t[%(asctime)s]\033[0m\n\n%(message)s\n"
    )
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    return logger


logger = setup_logger()
