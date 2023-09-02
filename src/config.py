from decouple import config as env

API_HOST = "http://mycodo/api/"
API_KEY = env("API_KEY")

