import logzero
import config

def get_logger():
    """ Setup logger """
    logger = logzero.setup_logger(name="mycodo-exporter", level=config.LOG_LEVEL, logfile=config.LOG_FILE, fileLoglevel=config.FILE_LOG_LEVEL, maxBytes=1000000, backupCount=3)
    return logger