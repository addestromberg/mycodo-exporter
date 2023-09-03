from decouple import config as env
import logzero
API_HOST = "http://mycodo/"
API_KEY = env("API_KEY")

LOG_LEVEL = logzero.DEBUG
LOG_FILE = "./logs/exporter.log"
FILE_LOG_LEVEL = logzero.WARNING

EXPORT_MEASUREMENTS = ["INPUTS", "OUTPUTS", "PIDS"]