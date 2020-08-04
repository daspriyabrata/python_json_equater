class FileManager:
    def __init__(self, _file_path):
        self._file_path = _file_path

    def read_file(self):
        with open(self._file_path, 'r') as _file:
            _data = [_.strip() for _ in _file.readlines()]
            _file.close()
        return _data
