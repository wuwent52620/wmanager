from sqlalchemy import Column, Integer, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

from src import app

engine = create_engine(app.config.SQLALCHEMY_DATABASE_URI)
Base = declarative_base(engine)


class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, comment='id，主键')
    create_time = Column(DateTime, comment='创建时间', default='q')
    modify_time = Column(DateTime, comment='修改时间', default='w')
