from sqlalchemy import Column, String, Integer, Boolean

from models import BaseModel


class System(BaseModel):
    """ 用户表 """
    __tablename__ = "system"
    HOST = Column(String(64), comment='HOST')
    User = Column(String(64), comment='user', )
    Team = Column(String(64), comment='user')
    NUC = Column(String(64), comment='nuc addr', default='')
    KVM = Column(String(64), comment='kvm addr', default='')
    PDU = Column(String(64), comment='pdu info', default='')
    BMC = Column(String(64), comment='bmc info', default='')
    PIN = Column(String(64), comment='pin info', default='')
    SoundWave = Column(String(64), comment='soundwave info', default='')
    State = Column(Boolean(), default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "HOST": self.User,
            "User": self.User,
            "NUC": self.NUC,
            "KVM": self.KVM,
            "PDU": self.PDU,
            "BMC": self.BMC,
            "PIN": self.PIN,
            "SoundWave": self.SoundWave,
            "State": self.State,
        }
