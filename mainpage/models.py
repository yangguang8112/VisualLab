from sqlalchemy import Column, Integer, String, TIMESTAMP
from mainpage.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)

#温度


class Sample(Base):
    __tablename__ = 'sample_info'
    id = Column(Integer, primary_key=True)
    chip_name = Column(String(100))
    lane_name = Column(String(100))
    machine_id = Column(Integer)
    sample_type = Column(String(100))
    DNB_name = Column(String(100))
    library_name = Column(String(100))
    created_time = Column(TIMESTAMP)
    sample_status = Column(String(100))
    finish_time = Column(TIMESTAMP)

    def __init__(self, chip_name=None, lane_name=None, machine_name=None, sample_type=None, DNB_id=None, \
        library_id=None, created_time=None, sample_status=None, finish_time=None):
        self.chip_name = chip_name
        self.lane_name = lane_name
        self.machine_name = machine_name
        self.sample_type = sample_type
        self.DNB_id = DNB_id
        self.library_id = library_id
        self.created_time = created_time
        self.sample_status = sample_status
        self.finish_time = finish_time
    
    def __repr__(self):
        return 'wait.....'


class Machine(Base):
    __tablename__ = 'machine'
    id = Column(Integer, primary_key=True)
    machine_name = Column(String(100))
    machine_type = Column(String(100))

    def __init__(self, machine_name=None, machine_type=None):
        self.machine_name = machine_name
        self.machine_type = machine_type
    
    def __repr__(self):
        return 'wait'

class RawData(Base):
    __tablename__ = 'raw_data'
    id = Column(Integer, primary_key=True)
    sample_id = Column(Integer)

    def __init__(self, sample_id=None):
        self.sample_id = sample_id
    
    def __repr__(self):
        return 'wait'

