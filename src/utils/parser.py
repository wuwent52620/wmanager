import configparser
import os
from collections import namedtuple


class Parser(object):
    def __init__(self, env='develop'):
        base_path = os.path.dirname(os.path.dirname(__file__))
        env_dir = os.path.join(base_path, "config")
        env_file = os.path.join(env_dir, f"{env}.ini")
        _parser = configparser.ConfigParser()
        _parser.read(env_file)
        self.__config = _parser.sections()
        self.__items = lambda x: _parser.items(x)
        self.__options = lambda x: _parser.options(x)
        self.__parse()

    def __parse(self):
        all_sections = self.__config
        for attr in all_sections:
            _attr = self.__items(attr)
            named_tuple = namedtuple('_', self.__options(attr))
            obj = named_tuple(**{k: v for k, v in _attr})
            setattr(self, attr, obj)
