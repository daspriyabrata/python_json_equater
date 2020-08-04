import os
from concurrent.futures import ThreadPoolExecutor
import logging

from utils.df_comparater import DFComparator
from utils.file_manager import FileManager
from g_libs.print_formatter import bcolors
from utils.httprequestmanager import HttpRequest


LOGGER = logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO, datefmt="%H:%M:%S")
logger = logging.getLogger(__name__)


class Gojeck_API:
    def __int__(self):
        pass

    @staticmethod
    def __test_api_comparator(_end_point, _target_end_point):
        _api_handler = HttpRequest(_end_point)
        _target_api_handler = HttpRequest(_target_end_point)
        _dfc = DFComparator()
        try:
            assert _dfc.compare_json(_api_handler.get_details().json(), _target_api_handler.get_details().json())
            logger.info(f'{bcolors.OKGREEN}{_end_point} equals {_target_end_point}{bcolors.ENDC}')
        except AssertionError:
            logger.info(f'{bcolors.FAIL}{_end_point} not equals {_target_end_point}{bcolors.ENDC}')

    def run(self):
        _first_file = FileManager(os.getcwd() + '/data/file1')
        _target_file = FileManager(os.getcwd() + '/data/file2')
        with ThreadPoolExecutor(max_workers=50) as _test_runner:
            _test_results = _test_runner.map(self.__test_api_comparator, _first_file.read_file(),
                                             _target_file.read_file())


if __name__ == '__main__':
    _api_test_runner = Gojeck_API()
    _api_test_runner.run()
