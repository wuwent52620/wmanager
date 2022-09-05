from random import randint

from faker import Faker

fake = Faker()


class FakeGen(object):
    def __init__(self, attr, **kwargs):
        self.__attr = attr
        self.kwargs = kwargs

    def __iter__(self):
        return self

    def __next__(self):
        if isinstance(self.__attr, str):
            return eval(f"fake.{self.__attr}(**self.kwargs)")
        else:
            return self.__attr()


class WFaker(object):
    date_time = FakeGen('date_time_this_year', before_now=True, after_now=False, tzinfo=None)
    host = FakeGen("ipv4_private", network=False, address_class=None)
    random_str_12 = FakeGen("pystr", min_chars=None, max_chars=12)
    random_int_1_3 = FakeGen("random_int", min=1, max=3)
    single_words_7 = FakeGen("sentence", nb_words=7, variable_nb_words=True, ext_word_list=None)
    custom_1_2 = FakeGen(lambda: randint(1, 2))
    custom_bool = FakeGen(lambda: bool(randint(0, 1)))

    def __init__(self):
        self.add_attr()
        super().__init__()

    @classmethod
    def add_attr(cls):
        cls.faker_attr_mapping = dict()
        for key, value in cls.__dict__.items():
            if isinstance(value, FakeGen):
                value = iter(value)
                cls.faker_attr_mapping[key] = value

    def data(self, *args, count=1):
        while count:
            need_data = list()
            for key in args:
                if key in self.faker_attr_mapping.keys():
                    need_data.append(self.faker_attr_mapping[key])
            _data = list()
            for value in need_data:
                _data.append(next(value))
            yield _data
            count -= 1
