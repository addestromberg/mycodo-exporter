import config
import requests
import json
from pprint import pprint
from utility import get_logger

logger = get_logger()

class MycodoApi:
    _host: str
    _api_key: str
    _headers: dict
    def __init__(self) -> None:
        self._host = config.API_HOST
        self._api_key = config.API_KEY
        self._headers = {"accept": "application/vnd.mycodo.v1+json",
                         "X-API-KEY": self._api_key}
        
    def get_input_devices(self):
        url = self._build_url(endpoint="inputs")
        result = requests.get(url=url, headers=self._headers)
        if result.status_code == 200:
            return json.loads(result.text)
        else:
            return None
        
    def get_output_devices(self):
        url = self._build_url(endpoint="outputs")
        result = requests.get(url=url, headers=self._headers)
        if result.status_code == 200:
            return json.loads(result.text)
        else:
            return None
    
    def get_pids(self):
        url = self._build_url(endpoint="pids")
        result = requests.get(url=url, headers=self._headers)
        if result.status_code == 200:
            return json.loads(result.text)
        else:
            return None
        
    def _build_url(self, endpoint: str) -> str:
        """
        Build the uri depending on endpoint

        Args:
            endpoint (str): the endpoint

        Returns:
            str: complete uri
        """
        return f"{self._host}api/{endpoint}/"