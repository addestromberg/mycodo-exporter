from decouple import config as env
import logzero
API_HOST = "http://mycodo/"
API_KEY = env("API_KEY")

LOG_LEVEL = logzero.DEBUG
LOG_FILE = "./logs/exporter.log"
FILE_LOG_LEVEL = logzero.WARNING

EXPORT_MEASUREMENTS = ["INPUTS", "OUTPUTS"]     # This is due to the API model.
PAST_SECONDS = 3600                                     # How old can the data be?

INTERVAL_SECONDS = 60                                   # How often to update metrics

SERVER_PORT = 8000