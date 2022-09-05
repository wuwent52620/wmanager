from collections import OrderedDict

from sqlalchemy import create_engine, delete, insert
from sqlalchemy.orm import sessionmaker

from models import system
from src import config
from utils.wfaker import WFaker

engine = create_engine(config['default'].SQLALCHEMY_DATABASE_URI, isolation_level="AUTOCOMMIT")

Session = sessionmaker(engine)

db_session = Session()

from manage import user


def bulk_insert(module, **kwargs):
    _data = [module(**single) for single in __gen_data(**kwargs)]
    with db_session.begin():
        db_session.add_all(_data)


def del_all(module):
    db_session.query(module).filter(module.id != -1).delete()
    db_session.close()


def __gen_data(**kw):
    kw = OrderedDict(**kw)
    fake_list = WFaker().data(*kw.values(), count=10)
    multi_data = (zip(kw.keys(), single) for single in fake_list)
    for item in multi_data:
        yield {k: v for k, v in item}


if __name__ == '__main__':
    # print(OrderedDict(**{'a': 1, 'b': 2, 'c': 3}).keys())
    # data = {'username': "random_str_12", "password": "random_str_12", "level": "random_int_1_3"}
    data = {'HOST': "host", "User": "random_str_12", "Team": "custom_1_2", "NUC": 'host', "KVM": "host", "PDU": "host",
            "BMC": "host", "PIN": "random_str_12", "SoundWave": 'random_str_12', "State": "custom_bool"}
    bulk_insert(system.System, **data)
    # del_all(user.User)
