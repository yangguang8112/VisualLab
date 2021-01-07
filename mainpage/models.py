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
    lane_id = Column(String(100))
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
    Q30_read1 = Column(Float)
    Q30_read2 = Column(Float)
    Q30_total = Column(Float)
    Q20 = Column(Float)
    totalreads_M = Column(Float)
    Lag1 = Column(Float)
    Lag2 = Column(Float)
    Lag_table = Column(Text)
    Runon1 = Column(Float)
    Runon2 = Column(Float)
    Runon_table = Column(Text)
    cycle_N_max = Column(Float)
    Error_rate_est = Column(Float)
    ChipProductivity = Column(Float)
    ImageAre = Column(Float)
    Offset_table = Column(Text)
    RecoverValue_A = Column(Float)
    RecoverValue_G = Column(Float)
    RecoverValue_C = Column(Float)
    RecoverValue_T = Column(Float)
    RecoverValue_AVG = Column(Float)
    RecoverValue_AGCT_table = Column(Text)
    Intensity_of_All_DNB_table = Column(Text)
    RHO_Intensity_table = Column(Text)
    Background_Intensity_table = Column(Text)
    SNR_table = Column(Text)
    BIC = Column(Float)
    BIC_table = Column(Text)
    FIT = Column(Float)
    FIT_table = Column(Text)

    '''
    def __init__(self, sample_id=None, ceshi=None):
        self.sample_id = sample_id
        self.ceshi = ceshi
    
    def __repr__(self):
        return 'wait'
    '''

class PipeRes(Base):
    __tablename__ = 'pipe_res'
    id = Column(Integer, primary_key=True)
    create_date = Column(DateTime, server_default=func.now())
    project_name = Column(String(100))
    cluster_name = Column(String(100))
    sample_id = Column(Integer, ForeignKey('sample_info.id'))
    PipelineVersion = Column(String(100))
    sample_name = Column(String(100))
    TotalReads_Mb = Column(Float)
    TotalBases_Gb = Column(Float)
    Read1_Q20_rate = Column(Float)
    Read2_Q20_rate = Column(Float)
    Read1_Q30_rate = Column(Float)
    Read2_Q30_rate = Column(Float)
    Read1_A_rate = Column(Float)
    Read1_T_rate = Column(Float)
    Read1_G_rate = Column(Float)
    Read1_C_rate = Column(Float)
    Read2_A_rate = Column(Float)
    Read2_T_rate = Column(Float)
    Read2_G_rate = Column(Float)
    Read2_C_rate = Column(Float)
    Read1BaseDiversity_AT = Column(Float)
    Read1BaseDiversity_GC = Column(Float)
    Read2BaseDiversity_AT = Column(Float)
    Read2BaseDiversity_GC = Column(Float)
    Max_N_content = Column(Float)
    GC_rate = Column(Float)
    clean_raw_rate = Column(Float)
    EqualReads = Column(String(100))
    ReferenceVersion = Column(String(100))
    MappingRate = Column(Float)
    UniqueRate = Column(Float)
    DuplicateRate = Column(Float)
    MismatchRate = Column(Float)
    AveInsertSize = Column(Float)
    SdInsertSize = Column(Float)
    chr1_AveDepth_X = Column(Float)
    chr2_AveDepth_X = Column(Float)
    chr3_AveDepth_X = Column(Float)
    chr4_AveDepth_X = Column(Float)
    chr5_AveDepth_X = Column(Float)
    chr6_AveDepth_X = Column(Float)
    chr7_AveDepth_X = Column(Float)
    chr8_AveDepth_X = Column(Float)
    chr9_AveDepth_X = Column(Float)
    chr10_AveDepth_X = Column(Float)
    chr11_AveDepth_X = Column(Float)
    chr12_AveDepth_X = Column(Float)
    chr13_AveDepth_X = Column(Float)
    chr14_AveDepth_X = Column(Float)
    chr15_AveDepth_X = Column(Float)
    chr16_AveDepth_X = Column(Float)
    chr17_AveDepth_X = Column(Float)
    chr18_AveDepth_X = Column(Float)
    chr19_AveDepth_X = Column(Float)
    chr20_AveDepth_X = Column(Float)
    chr21_AveDepth_X = Column(Float)
    chr22_AveDepth_X = Column(Float)
    chrX_AveDepth_X = Column(Float)
    chrY_AveDepth_X = Column(Float)
    chrM_AveDepth_X = Column(Float)
    AveDepth_X = Column(Float)
    X1_Coverage_rate = Column(Float)
    X5_Coverage_rate = Column(Float)
    X10_Coverage_rate = Column(Float)
    X20_Coverage_rate = Column(Float)
    X30_Coverage_rate = Column(Float)
    X40_Coverage_rate = Column(Float)
    X50_Coverage_rate = Column(Float)
    X60_Coverage_rate = Column(Float)
    X70_Coverage_rate = Column(Float)
    X80_Coverage_rate = Column(Float)
    X90_Coverage_rate = Column(Float)
    X100_Coverage_rate = Column(Float)
    SdCoverage = Column(Float)
    SNP_Number = Column(Integer)
    SNP_in_dbSNP = Column(Integer)
    SNP_in_1KGP3 = Column(Integer)
    SNP_in_gnomAD_exomes = Column(Integer)
    SNP_in_gnomAD_genomes = Column(Integer)
    SNP_in_TOPMed = Column(Integer)
    SNP_in_ChinaMAP = Column(Integer)
    Novel_SNP = Column(Integer)
    Homozygous_SNP = Column(Integer)
    Heterozygous_SNP = Column(Integer)
    HIGH_impact_SNP = Column(Integer)
    MODERATE_impact_SNP = Column(Integer)
    LOW_impact_SNP = Column(Integer)
    MODIFIER_impact_SNP = Column(Integer)
    Het_Hom = Column(Float)
    Ti_Tv = Column(Float)
    INDEL_Number = Column(Integer)
    INDEL_in_dbSNP = Column(Integer)
    INDEL_in_1KGP3 = Column(Integer)
    INDEL_in_gnomAD_exomes = Column(Integer)
    INDEL_in_gnomAD_genomes = Column(Integer)
    INDEL_in_TOPMed = Column(Integer)
    INDEL_in_ChinaMAP = Column(Integer)
    Novel_INDEL = Column(Integer)
    Homozygous_INDEL = Column(Integer)
    Heterozygous_INDEL = Column(Integer)
    HIGH_impact_INDEL = Column(Integer)
    MODERATE_impact_INDEL = Column(Integer)
    LOW_impact_INDEL = Column(Integer)
    MODIFIER_impact_INDEL = Column(Integer)
    CNV_CNVnator_Number = Column(Integer)
    CNV_CNVnator_DUP_Length = Column(Integer)
    CNV_CNVnator_DEL_Length = Column(Integer)
    CNV_CNVnator_Anno_Number = Column(Integer)
    SV_lumpy_Number = Column(Integer)
    SV_lumpy_Anno_Number = Column(Integer)
    SV_delly_Number = Column(Integer)
    SV_delly_Anno_Number = Column(Integer)
    SV_manta_Number = Column(Integer)
    SV_manta_Anno_Number = Column(Integer)
    SV_MELT_Number = Column(Integer)
    SV_MELT_Anno_Number = Column(Integer)
    MS_consistency_rate = Column(Float)
    GeneticSex = Column(String(100))
    contamination_rate = Column(Float)
    mtDNAhaplotype = Column(String(100))
    Judge = Column(String(100))
    Note = Column(Text)


class JobDetail(Base):
    __tablename__ = 'job_detail'
    id = Column(Integer, primary_key=True)
    create_date = Column(DateTime, server_default=func.now())
    project_name = Column(String(100))
    cluster_name = Column(String(100))
    PipelineVersion = Column(String(100))
    Job_ID = Column(String(100))
    Job_Name = Column(String(100))
    Module = Column(String(200))
    Step = Column(String(100))
    Sample = Column(String(100))
    Thread = Column(Integer)
    Start_Time = Column(TIMESTAMP)
    End_Time = Column(TIMESTAMP)
    Cpu_Utilized_s = Column(Float)
    Wall_clock_Time_s = Column(Float)
    Core_walltime_s = Column(Float)
    Ratio = Column(Float)
    Maxmem_K = Column(Float)