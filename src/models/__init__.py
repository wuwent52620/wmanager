from sqlalchemy import Column, Integer, DateTime, create_engine, DATETIME
from sqlalchemy.ext.declarative import declarative_base

from src import app
from utils.format import Date

engine = create_engine(app.config.SQLALCHEMY_DATABASE_URI)
Base = declarative_base(engine)

date_now = Date().now


class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, comment='id，主键', autoincrement=True)
    create_time = Column(DateTime, comment='创建时间', default=date_now())
    modify_time = Column(DateTime, comment='修改时间', default=date_now())

    # # 新增
    # def insert(self, tbk_good):
    #     self.session.add(tbk_good)
    #     self.session.commit()
    #     return tbk_good.id
    #
    # # 批量新增
    # def insert_batch(self, tbk_good_array):
    #     self.session.add_all(tbk_good_array)
    #     self.session.commit()
    #
    # # 修改
    # def update(self, goods_id, **kwargs):
    #     self.session.query(TaoBaoKeGoods).filter(TaoBaoKeGoods.id == goods_id).update(kwargs)
    #     self.session.commit()
    #
    # # 删除
    # def delete_by_id(self, goods_id):
    #     self.session.query(TaoBaoKeGoods).filter(TaoBaoKeGoods.id == goods_id).delete()
    #     self.session.commit()
    #
    # # 读取一条
    # def read_one(self):
    #     return self.session.query(TaoBaoKeGoods).first()
    #
    # # 根据ID读取一条
    # def read_one_by_id(self, goods_id):
    #     return self.session.query(TaoBaoKeGoods).filter(TaoBaoKeGoods.id == goods_id).first()
    #
    # # 读取所有
    # def read_all(self):
    #     return self.session.query(TaoBaoKeGoods).all()
    #
    # # 读取所有通过filter
    # def read_all_by_filter(self, *filter_clauses):
    #     for filter_clause in filter_clauses:
    #         print(filter_clause)
    #     return self.session.query(TaoBaoKeGoods).filter(*filter_clauses).all()
    #
    # # 读取所有通过filter_by
    # def read_all_by_filter_by(self, **filter_by_clauses):
    #     for filter_by_key in filter_by_clauses:
    #         print(filter_by_key, filter_by_clauses[filter_by_key])
    #     return self.session.query(TaoBaoKeGoods).filter_by(**filter_by_clauses).all()
    #
    # # 读取所有分页
    # def read_all_pagination(self, *order_by_clauses, offset=0, limit=10):
    #     for order_by_clause in order_by_clauses:
    #         print(order_by_clause)
    #     return self.session.query(TaoBaoKeGoods).order_by(*order_by_clauses).offset(offset).limit(limit).all()
