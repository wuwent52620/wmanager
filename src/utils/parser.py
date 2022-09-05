import configparser
import hashlib
import os
from collections import namedtuple

from sanic import Sanic


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


def md5(s, key=None):
    def handle(data):
        data = str(data + salt).encode()
        res = hashlib.md5(data)
        return res.hexdigest()

    salt = Sanic.get_app().config.SECRET
    if key:
        if isinstance(s, dict):
            if s.get(key):
                s[key] = handle(s[key])
        elif isinstance(s, list):
            for _s in s:
                if _s.get(key):
                    _s[key] = handle(_s[key])
        return s
