import os
from sanic.config import Config
from elasticsearch6 import Elasticsearch


class ProductionConfig:
    """Uses production database server."""
    ES = Elasticsearch('http://172.16.0.147:9200')

    DIALECT = 'mysql'
    DRIVER = 'aiomysql'
    USERNAME = 'user'
    PASSWORD = '*************'
    HOST = 'rm-****'
    PORT = '3306'
    DATABASE = '****'

    SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8mb4'.format(
        DIALECT,
        DRIVER,
        USERNAME,
        PASSWORD,
        HOST,
        PORT,
        DATABASE
    )


class DevelopmentConfig:
    APP_ID = '*************'
    APP_SECRET = '*******************'
    # 密钥配置
    SECRET_KEY = '1111222'
    DEBUG = True
    ES = Elasticsearch('http://10.168.1.216:9200')

    SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8mb4'.format(
        'mysql',
        'aiomysql',
        'root',
        '123456',
        '192.168.2.81',
        '3307',
        'su'
    )


config = {
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
