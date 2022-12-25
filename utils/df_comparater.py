class DFComparator:
    def __init__(self):
        pass

    @staticmethod
    def __sorter(_json):
        def sorter(_json):
            if isinstance(_json, dict):
                return sorted((_k, sorter(_v)) for _k, _v in _json.items())
            elif isinstance(_json, list):
                return sorted(sorter(_item) for _item in _json)
            else:
                return _json

        return sorter(_json)

    def compare_json(self, _json, _other_json):
        if isinstance(_json, dict):
            if not (isinstance(_other_json, dict)):
                return False
            _is_alike = self.__sorter(_json) == self.__sorter(_other_json)
            return True if _is_alike else False
        elif isinstance(_json, list):
            if not (isinstance(_other_json, list)):
                return False
            _is_alike = self.__sorter(_json) == self.__sorter(_other_json)
            return True if _is_alike else False
        else:
            return _json == _other_json
