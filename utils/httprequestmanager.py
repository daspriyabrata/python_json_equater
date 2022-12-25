import logging
from requests import Session
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError, HTTPError, Timeout
from g_libs.print_formatter import bcolors

logger = logging.getLogger(__name__)


class HttpRequest:
    def __init__(self, _url):
        self._url = _url

    def get_details(self):
        session = Session()
        Gojek_adapter = HTTPAdapter(max_retries=3)
        session.mount(self._url, Gojek_adapter)
        try:
            return session.get(url=self._url, timeout=(2, 5))
        except ConnectionError as ce:
            logger.info(f'{bcolors.WARNING}Connection Error:{ce} {bcolors.ENDC}')
        except HTTPError as he:
            logger.info(f'{bcolors.WARNING}HTTP Error: {he}{bcolors.ENDC}')
        except Timeout as t:
            logger.info(f'{bcolors.WARNING}Timeout Error: {t}{bcolors.ENDC}')
