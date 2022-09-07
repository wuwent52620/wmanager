import json
import os

from elasticsearch6 import Elasticsearch

from utils.parser import Parser

basedir = os.path.abspath(os.path.dirname(__file__))


class AppConfig:
    WEBSOCKET_MAX_SIZE = 2 ** 20
    WEBSOCKET_MAX_QUEUE = 32
    WEBSOCKET_READ_LIMIT = 2 ** 16
    WEBSOCKET_WRITE_LIMIT = 2 ** 16
    WEBSOCKET_PING_INTERVAL = 20
    WEBSOCKET_PING_TIMEOUT = 20

    def __init__(self, env, debug=True):
        self.APP_ID = '*************'
        self.APP_SECRET = '*******************'
        # 密钥配置
        self.SECRET_KEY = 'W_MANAGER_WWT'
        self.DEBUG = debug
        parser = Parser(env=env)
        """Uses production database server."""
        self.ES = Elasticsearch(f'http://{parser.es.host}:{parser.es.port}')

        self.SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8mb4'.format(
            'mysql',
            'pymysql',
            parser.mysql.user,
            parser.mysql.password,
            parser.mysql.host,
            parser.mysql.port,
            parser.mysql.db
        )
        self.SQLALCHEMY_DATABASE_AIO = '{}+{}://{}:{}@{}:{}/{}?charset=utf8mb4'.format(
            'mysql',
            'aiomysql',
            parser.mysql.user,
            parser.mysql.password,
            parser.mysql.host,
            parser.mysql.port,
            parser.mysql.db
        )
        self.SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'migrations')
        self.REDIS = {
            "host": parser.redis.host,
            "port": parser.redis.port,
            "poolsize": parser.redis.poolsize,
            "expire": parser.redis.expire
        }


config = {
    'production': AppConfig('product', False),
    'default': AppConfig('develop1')
}
