from functools import lru_cache
from iriurisk_test.app_config import get_config
import logging


@lru_cache
def get_logger() -> logging.Logger:
    """ """
    config = get_config()
    _logger = logging.getLogger("api_logger")
    _logger.setLevel(getattr(logging, config.log_level))

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s"
    )

    # StreamHandler
    sh = logging.StreamHandler()
    sh.setFormatter(formatter)
    _logger.addHandler(sh)

    return _logger


logger = get_logger()
