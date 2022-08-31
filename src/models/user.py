from sqlalchemy import Column, String, Integer

from models import BaseModel


class User(BaseModel):
    """ 用户表 """
    __tablename__ = "user"
    username = Column(String(64), comment='账号')
    password = Column(String(64), comment='密码')
    level = Column(Integer, comment='等级')

    def to_dict(self):
        return {"id": self.id, "username": self.username, "password": self.password, 'level': self.level}
