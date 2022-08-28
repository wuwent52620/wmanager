from sqlalchemy import Column, String, Integer

from models import BaseModel


class System(BaseModel):
    """ 用户表 """
    __tablename__ = "system"
    ip = Column(String(64), comment='IP')
    password = Column(String(64), comment='密码')
    username = Column(String(64), comment='用户')

    def to_dict(self):
        return {"id": self.id, "username": self.username, "password": self.password}
