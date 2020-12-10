from sqlalchemy import Column, Integer, String, TIMESTAMP, Float, Text, ForeignKey, func, DateTime
from mainpage.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    create_date = Column(DateTime, server_default=func.now())
    modify_date = Column(DateTime, onupdate=func.utc_timestamp())

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)

#温度


class Sample(Base):
    __tablename__ = 'sample_info'
    id = Column(Integer, primary_key=True)
    create_date = Column(DateTime, server_default=func.now())
    # python的这个接口没什么卵用，还是得用原生sql创建表才会自动更新
    modify_date = Column(DateTime, server_default=func.now(), onupdate=func.now())

    sample_origin_code = Column(String(100))
    sample_code = Column(String(100))
    sample_dr_count = Column(Integer)
    sample_origin_conc = Column(Float)
    zhijian_ban_code = Column(String(100))
    zhijian_kongwei = Column(String(100))
    library_kit_code = Column(String(100))
    library_ban_code = Column(String(100))
    library_kongwei = Column(String(100))
    library_name = Column(String(100))
    barcode = Column(String(100))
    adapter_conc = Column(Float)
    library_conc = Column(Float)
    library_vol = Column(Float)
    out_library_date = Column(TIMESTAMP)
    jianku_beizhu = Column(Text)

    shangji_kit_code = Column(String(100))
    DNB_dr_count = Column(Integer)
    DNB_name = Column(String(100))
    DNB_conc = Column(Float)
    chip_name = Column(String(100))
    makeload_operator = Column(String(100))
    makeload_date = Column(TIMESTAMP)
    makeload_beizhu = Column(Text)

    machine_code = Column(String(100))
    lane_id = Column(Integer)
    seq_type = Column(String(100))
    seq_operator = Column(String(100))
    seq_date = Column(TIMESTAMP)
    seq_beizhu = Column(Text)

    def __repr__(self):
        return {'sample_id': self.id}
'''
    def __init__(self, sample_origin_code=None, sample_dr_count=None, sample_origin_conc=None, \
        zhijian_ban_code=None, zhijian_kongwei=None, library_kit_code=None, library_ban_code=None, \
        library_kongwei=None, library_name=None, barcode=None, adapter_conc=None, library_conc=None, \
        library_vol=None, out_library_date=None, jianku_beizhu=None, shangji_kit_code=None, \
        DNB_dr_count=None, DNB_name=None, DNB_conc=None, chip_name=None, makeload_operator=None, \
        makeload_date=None, makeload_beizhu=None, machine_code=None, lane_id=None, seq_type=None, \
        seq_operator=None, seq_date=None, seq_beizhu=None):
        self.sample_origin_code = sample_origin_code
        self.sample_dr_count = sample_dr_count
        self.sample_origin_conc = sample_origin_conc
        self.zhijian_ban_code = zhijian_ban_code
        self.zhijian_kongwei = zhijian_kongwei
        self.library_kit_code = library_kit_code
        self.library_ban_code = library_ban_code
        self.library_kongwei = library_kongwei
        self.library_name = library_name
        self.barcode = barcode
        self.adapter_conc = adapter_conc
        self.library_conc = library_conc
        self.library_vol = library_vol
        self.out_library_date = out_library_date
        self.jianku_beizhu = jianku_beizhu
        self.shangji_kit_code = shangji_kit_code
        self.DNB_dr_count = DNB_dr_count
        self.DNB_name = DNB_name
        self.DNB_conc = DNB_conc
        self.chip_name = chip_name
        self.makeload_operator = makeload_operator
        self.makeload_date = makeload_date
        self.makeload_beizhu = makeload_beizhu
        self.machine_code = machine_code
        self.lane_id = lane_id
        self.seq_type = seq_type
        self.seq_operator = seq_operator
        self.seq_date = seq_date
        self.seq_beizhu = seq_beizhu
'''


class Machine(Base):
    __tablename__ = 'machine'
    id = Column(Integer, primary_key=True)
    machine_name = Column(String(100))
    machine_type = Column(String(100))

    def __init__(self, machine_name=None, machine_type=None):
        self.machine_name = machine_name
        self.machine_type = machine_type
    
    def __repr__(self):
        return {'machine_id': self.id}

class RawData(Base):
    __tablename__ = 'raw_data'
    id = Column(Integer, primary_key=True)
    create_date = Column(DateTime, server_default=func.now())
    modify_date = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
    sample_id = Column(Integer, ForeignKey('sample_info.id'))
    xiaji_date = Column(TIMESTAMP)
    split_rate = Column(Float)
    esr = Column(Float)
    basenun_G = Column(Float)
    GC = Column(Float)
    Q30_read2 = Column(Float)
    Q30_total = Column(Float)
    Q20 = Column(Float)
    totalreads_M = Column(Float)
    Lag = Column(Float)
    Runon = Column(Float)
    cycle_N_max = Column(Float)
    Error_rate_est = Column(Float)
    ChipProductivity = Column(Float)
    ImageAre = Column(Float)
    MaxOffsetX_MaxOffsetY = Column(Float)
    InitialOffsetX_InitialOffsetY = Column(Float)
    RecoverValue_A_G_T_C_AVG = Column(Float)
    Intensity_of_All_DNB = Column(Float)
    RHO_Intensity = Column(Float)
    Background_Intensity = Column(Float)
    SNR = Column(Float)
    BIC = Column(Float)
    FIT = Column(Float)

    '''
    def __init__(self, sample_id=None, ceshi=None):
        self.sample_id = sample_id
        self.ceshi = ceshi
    
    def __repr__(self):
        return 'wait'
    '''

