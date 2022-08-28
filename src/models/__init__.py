from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, comment='id，主键')
    create_time = Column(DateTime, comment='创建时间', default='q')
    modify_time = Column(DateTime, comment='修改时间', default='w')
