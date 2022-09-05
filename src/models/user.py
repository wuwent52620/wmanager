import json

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref

from models import BaseModel


class Team(BaseModel):
    __tablename__ = "team"
    teamname = Column(String(64), comment='账号')
    level = Column(Integer, comment='团队等级')

    def to_dict(self):
        return {
            "id": self.id,
            "teamname": self.teamname,
            'level': self.level,
        }


class User(BaseModel):
    """ 用户表 """
    __tablename__ = "user"
    username = Column(String(64), comment='账号')
    password = Column(String(64), comment='密码')
    level = Column(Integer, comment='个人等级', default=0)
    team_id = Column(Integer, ForeignKey("team.id"))
    team = relationship("Team", backref=backref('users', order_by=BaseModel.id))

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            'level': self.level,
            'teamId': self.team_id
        }
