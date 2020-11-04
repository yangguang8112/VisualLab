
DROP TABLE IF EXISTS raw_data;
DROP TABLE IF EXISTS qc_res;
DROP TABLE IF EXISTS align_res;
DROP TABLE IF EXISTS analy_res;

CREATE TABLE raw_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    chip_id TEXT NOT NULL,
    lane_id TEXT NOT NULL,
    created TIMESTAMP NOT NULL,
    split_rate FLOAT NOT NULL,
    esr FLOAT NOT NULL,
    basenun_G INTEGER NOT NULL,
    GC FLOAT NOT NULL,
    Q30_read2 FLOAT NOT NULL,
    Q30_total FLOAT NOT NULL,
    Q20 FLOAT NOT NULL,
    totalreads_M INTEGER NOT NULL,
    Lag FLOAT NOT NULL,
    Runon FLOAT NOT NULL,
    cycle_N_max FLOAT NOT NULL,
    Error_rate_est FLOAT NOT NULL,
    ChipProductivity FLOAT NOT NULL,
    ImageAre FLOAT NOT NULL,
    MaxOffsetX_MaxOffsetY FLOAT NOT NULL,
    InitialOffsetX_InitialOffsetY FLOAT NOT NULL,
    RecoverValue_A_G_T_C_AVG FLOAT NOT NULL,
    Intensity_of_All_DNB FLOAT NOT NULL,
    RHO_Intensity FLOAT NOT NULL,
    Background_Intensity FLOAT NOT NULL,
    SNR FLOAT NOT NULL,
    BIC FLOAT NOT NULL,
    FIT FLOAT NOT NULL
);

CREATE TABLE qc_res (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    chip_id TEXT NOT NULL,
    lane_id TEXT NOT NULL,
    sample_id TEXT NOT NULL,
    created TIMESTAMP NOT NULL,
    totalreads_Mb FLOAT NOT NULL,
    totalbases_Gb FLOAT NOT NULL,
    read1_Q20 FLOAT NOT NULL,
    read2_Q30 FLOAT NOT NULL,
    read1_A FLOAT NOT NULL,
    read1_T FLOAT NOT NULL,
    read1_G FLOAT NOT NULL,
    read1_C FLOAT NOT NULL,
    read2_A FLOAT NOT NULL,
    read2_T FLOAT NOT NULL,
    read2_G FLOAT NOT NULL,
    read2_C FLOAT NOT NULL,
    Read1BaseDiversity_AT FLOAT NOT NULL,
    Read1BaseDiversity_GC FLOAT NOT NULL,
    Read2BaseDiversity_AT FLOAT NOT NULL,
    Read2BaseDiversity_GC FLOAT NOT NULL,
    GC FLOAT NOT NULL,
    Clean_data_Raw_data FLOAT NOT NULL,
    EqualReads FLOAT NOT NULL
);

CREATE TABLE align_res(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    chip_id TEXT NOT NULL,
    lane_id TEXT NOT NULL,
    sample_id TEXT NOT NULL,
    ReferenceVersion TEXT NOT NULL,
    MappingRate FLOAT NOT NULL,
    UniqueRate FLOAT NOT NULL,
    DuplicateRate FLOAT NOT NULL,
    MismatchRate FLOAT NOT NULL,
    Depth FLOAT NOT NULL,
    c1X_Coverage FLOAT NOT NULL,
    c4X_Coverage FLOAT NOT NULL,
    c10X_Coverage FLOAT NOT NULL,
    c20X_Coverge FLOAT NOT NULL
);

CREATE TABLE analy_res(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    chip_id TEXT NOT NULL,
    lane_id TEXT NOT NULL,
    sample_id TEXT NOT NULL,
    SNP_Number FLOAT NOT NULL,
    Het_Hom FLOAT NOT NULL,
    Ti_Tv FLOAT NOT NULL,
    INDEL_Number FLOAT NOT NULL,
    CNV_Number FLOAT NOT NULL,
    CNV_DUP_Length FLOAT NOT NULL,
    CNV_DEL_Length FLOAT NOT NULL,
    CNV_Anno_Number FLOAT NOT NULL,
    SV_Number FLOAT NOT NULL,
    SV_Anno_Number FLOAT NOT NULL,
    MS_consistency FLOAT NOT NULL,
    GeneticSex FLOAT NOT NULL,
    contamination FLOAT NOT NULL,
    mtDNAhaplotype FLOAT NOT NULL
);