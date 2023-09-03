import logzero
import config
from slugify import slugify

def get_logger():
    """ Setup logger """
    logger = logzero.setup_logger(name="mycodo-exporter", level=config.LOG_LEVEL, logfile=config.LOG_FILE, fileLoglevel=config.FILE_LOG_LEVEL, maxBytes=1000000, backupCount=3)
    return logger

def format_name(data: str) -> str:
    """
    Safely format filenames from string

    Args:
        data (str): instrument exchange string

    Returns:
        str: safename for instrument
    """
    return slugify(data,
                   entities=True,
                   decimal=True,
                   hexadecimal=True,
                   max_length=0,
                   word_boundary=False,
                   separator='_',
                   save_order=False,
                   stopwords=(),
                   regex_pattern=None,
                   lowercase=True,
                   replacements=[[':', '_'], ['/', '_']],
                   allow_unicode=False
                )