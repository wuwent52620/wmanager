from sqlalchemy import Column, Integer, DateTime, create_engine, DATETIME, delete, insert, select, update, desc
from sqlalchemy.ext.declarative import declarative_base

from common.commons import json_response
from src import app
from utils.format import Date

engine = create_engine(app.config.SQLALCHEMY_DATABASE_URI)
Base = declarative_base(engine)

date_now = Date().now


class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, comment='id，主键', autoincrement=True)
    create_time = Column(DateTime, comment='创建时间', default=date_now())
    modify_time = Column(DateTime, comment='修改时间', default=date_now(), onupdate=date_now())

    # 新增一条
    @classmethod
    async def insert(cls, data, session=None):
        async with session.begin():
            obj = cls(**data)
            session.add_all([obj])
        return json_response(data=obj.to_dict())

    # 批量新增
    @classmethod
    async def insert_batch(cls, data, session=None):
        async with session.begin():
            objs = []
            for d in data:
                objs.append(cls(**d))
            session.add_all(objs)
        return json_response(data=[obj.to_dict() for obj in objs])

    # 修改一条
    @classmethod
    async def update(cls, obj_id, data, session=None):
        async with session.begin():
            stmt = update(cls).where(cls.id == obj_id).values(**data)
            await session.execute(stmt)
        return json_response(data=f"update {cls.__name__} ({obj_id}) successful")

    # 删除一条
    @classmethod
    async def delete_by_id(cls, obj_id, session=None):
        async with session.begin():
            stmt = delete(cls).where(cls.id == obj_id)
            await session.execute(stmt)
        return json_response(data=f"delete {cls.__name__} ({obj_id}) successful")

    # 批量删除
    @classmethod
    async def delete_batch(cls, obj_id_list, session=None):
        async with session.begin():
            stmt = delete(cls).filter(cls.id.in_(obj_id_list))
            await session.execute(stmt)
        return json_response(data=f"delete {cls.__name__} ({obj_id_list}) successful")

    # 读取一条
    @classmethod
    async def read_one(cls, session):
        async with session.begin():
            stmt = select(cls).filter().first()
            result = await session.execute(stmt)
            obj = result.scalar()

        if not obj:
            return json_response(data={})

        return json_response(data=obj.to_dict())

    # 根据ID读取一条
    @classmethod
    async def read_one_by_id(cls, obj_id, session):
        async with session.begin():
            stmt = select(cls).where(cls.id == obj_id)
            result = await session.execute(stmt)
            obj = result.scalar()

        if not obj:
            return json_response(data={})

        return json_response(data=obj.to_dict())

    # 读取所有
    @classmethod
    async def read_all(cls, session):
        async with session.begin():
            stmt = select(cls).filter()
            result = await session.execute(stmt)
            objs = result.fetchall()

        if not objs:
            return json_response(data={})

        return json_response(data=[obj[0].to_dict() for obj in objs], total=len(objs))

    # 读取所有通过filter
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

    # 读取所有分页
    @classmethod
    async def read_all_pagination(cls, data, session=None):
        page = data.get('page') or 1
        size = data.get('size') or 10
        order_by_clauses = data.getlist('order') or []
        order_by_clauses = list(order_by_clauses)
        for idx, value in enumerate(order_by_clauses):
            if value.startswith('-'):
                order_by_clauses[idx] = desc(getattr(cls, value[1:]))
            else:
                order_by_clauses[idx] = getattr(cls, value)
        page = int(page)
        size = int(size)
        if page < 1:
            return json_response(data={})
        offset = (page - 1) * size
        limit = size
        async with session.begin():
            stmt = select(cls).order_by(*order_by_clauses)
            result = await session.execute(stmt)
            length = result.raw.rowcount
            stmt = select(cls).order_by(*order_by_clauses).offset(offset).limit(limit)
            result = await session.execute(stmt)
            objs = result.fetchall()

        if not objs:
            return json_response(data={})
        prev_page = {"page": page - 1, "limit": limit}
        next_page = {"offset": page + 1, "limit": limit}
        return json_response(data=[obj[0].to_dict() for obj in objs], total=length, prev_page=prev_page,
                             next_page=next_page)
