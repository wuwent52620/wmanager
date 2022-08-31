import os

from elasticsearch6 import Elasticsearch

from utils.parser import Parser

basedir = os.path.abspath(os.path.dirname(__file__))


class ProductionConfig:
    parser = Parser(env='product')
    """Uses production database server."""
    ES = Elasticsearch(f'http://{parser.es.host}:{parser.es.port}')

    SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8mb4'.format(
        'mysql',
        'pymysql',
        parser.mysql.user,
        parser.mysql.password,
        parser.mysql.host,
        parser.mysql.port,
        parser.mysql.db
    )
    SQLALCHEMY_DATABASE_AIO = '{}+{}://{}:{}@{}:{}/{}?charset=utf8mb4'.format(
        'mysql',
        'aiomysql',
        parser.mysql.user,
        parser.mysql.password,
        parser.mysql.host,
        parser.mysql.port,
        parser.mysql.db
    )
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'migrations')
    REDIS = {
        "host": parser.redis.host,
        "port": parser.redis.port,
        "poolsize": parser.redis.poolsize,
        "expire": parser.redis.expire
    }


class DevelopmentConfig:
    parser = Parser(env='develop1')
    APP_ID = '*************'
    APP_SECRET = '*******************'
    # 密钥配置
    SECRET_KEY = '123456'
    DEBUG = True
    ES = Elasticsearch(f'http://{parser.es.host}:{parser.es.port}')

    SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8mb4'.format(
        'mysql',
        'pymysql',
        parser.mysql.user,
        parser.mysql.password,
        parser.mysql.host,
        parser.mysql.port,
        parser.mysql.db
    )
    SQLALCHEMY_DATABASE_AIO = '{}+{}://{}:{}@{}:{}/{}?charset=utf8mb4'.format(
        'mysql',
        'aiomysql',
        parser.mysql.user,
        parser.mysql.password,
        parser.mysql.host,
        parser.mysql.port,
        parser.mysql.db
    )
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'migrations')
    REDIS = {
        "host": parser.redis.host,
        "port": parser.redis.port,
        "poolsize": parser.redis.poolsize,
        "expire": parser.redis.expire
    }


config = {
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
