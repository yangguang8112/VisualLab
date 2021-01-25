DROP TABLE IF EXISTS sample_info;
DROP TABLE IF EXISTS raw_data;
DROP TABLE IF EXISTS qc_res;
DROP TABLE IF EXISTS align_res;
DROP TABLE IF EXISTS analy_res;

/*创建表带自动更新功能
*/
CREATE DATABASE IF NOT EXISTS visualDB DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
use visualDB;
CREATE TABLE `sample_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `modify_date` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `sample_origin_code` varchar(100) DEFAULT NULL,
  `sample_code` varchar(100) DEFAULT NULL,
  `sample_dr_count` int(11) DEFAULT NULL,
  `sample_origin_conc` float DEFAULT NULL,
  `zhijian_ban_code` varchar(100) DEFAULT NULL,
  `zhijian_kongwei` varchar(100) DEFAULT NULL,
  `library_kit_code` varchar(100) DEFAULT NULL,
  `library_ban_code` varchar(100) DEFAULT NULL,
  `library_kongwei` varchar(100) DEFAULT NULL,
  `library_name` varchar(100) DEFAULT NULL,
  `barcode` varchar(100) DEFAULT NULL,
  `adapter_conc` float DEFAULT NULL,
  `library_conc` float DEFAULT NULL,
  `library_vol` float DEFAULT NULL,
  `out_library_date` timestamp NULL DEFAULT NULL,
  `jianku_beizhu` text,
  `shangji_kit_code` varchar(100) DEFAULT NULL,
  `DNB_dr_count` int(11) DEFAULT NULL,
  `DNB_name` varchar(100) DEFAULT NULL,
  `DNB_conc` float DEFAULT NULL,
  `chip_name` varchar(100) DEFAULT NULL,
  `makeload_operator` varchar(100) DEFAULT NULL,
  `makeload_date` timestamp NULL DEFAULT NULL,
  `makeload_beizhu` text,
  `machine_code` varchar(100) DEFAULT NULL,
  `lane_id` varchar(100) DEFAULT NULL,
  `seq_type` varchar(100) DEFAULT NULL,
  `seq_operator` varchar(100) DEFAULT NULL,
  `seq_date` timestamp NULL DEFAULT NULL,
  `seq_beizhu` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

CREATE TABLE `raw_data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `modify_date` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `sample_id` int(11) DEFAULT NULL,
  `xiaji_date` timestamp NULL DEFAULT NULL,
  `split_rate` float DEFAULT NULL,
  `esr` float DEFAULT NULL,
  `basenun_G` real DEFAULT NULL,
  `GC` float DEFAULT NULL,
  `Q30_read1` real DEFAULT NULL,
  `Q30_read2` real DEFAULT NULL,
  `Q30_total` real DEFAULT NULL,
  `Q20` real DEFAULT NULL,
  `totalreads_M` real DEFAULT NULL,
  `Lag1` float DEFAULT NULL,
  `Lag2` float DEFAULT NULL,
  `Lag_table` text,
  `Runon1` float DEFAULT NULL,
  `Runon2` float DEFAULT NULL,
  `Runon_table` text,
  `cycle_N_max` float DEFAULT NULL,
  `Error_rate_est` float DEFAULT NULL,
  `ChipProductivity` float DEFAULT NULL,
  `ImageAre` float DEFAULT NULL,
  `Offset_table` text,
  `RecoverValue_A` float DEFAULT NULL,
  `RecoverValue_G` float DEFAULT NULL,
  `RecoverValue_T` float DEFAULT NULL,
  `RecoverValue_C` float DEFAULT NULL,
  `RecoverValue_AVG` float DEFAULT NULL,
  `RecoverValue_AGCT_table` text,
  `Intensity_of_All_DNB_table` text,
  `RHO_Intensity_table` text,
  `Background_Intensity_table` text,
  `SNR_table` text,
  `BIC` float DEFAULT NULL,
  `BIC_table` text,
  `FIT` float DEFAULT NULL,
  `FIT_table` text,
  PRIMARY KEY (`id`),
  KEY `sample_id` (`sample_id`),
  CONSTRAINT `raw_data_ibfk_1` FOREIGN KEY (`sample_id`) REFERENCES `sample_info` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

/**/





/*created 应该是时间类型，需要修改
*/

CREATE TABLE sample_info (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    chip_name TEXT NOT NULL,
    lane_name TEXT NOT NULL,
    machine_name TEXT NOT NULL,
    sample_name TEXT NOT NULL,
    sample_type TEXT NOT NULL,
    DNB TEXT NOT NULL,
    library TEXT NOT NULL,
    created TIMESTAMP  NOT NULL,
    sample_status TEXT NOT NULL,
    finish_time TIMESTAMP  NOT NULL,
);

CREATE TABLE raw_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sample_id INTEGER NOT NULL,
    created TIMESTAMP  NOT NULL,
    split_rate FLOAT NOT NULL,
    esr FLOAT NOT NULL,
    basenun_G FLOAT NOT NULL,
    GC FLOAT NOT NULL,
    Q30_read2 FLOAT NOT NULL,
    Q30_total FLOAT NOT NULL,
    Q20 FLOAT NOT NULL,
    totalreads_M FLOAT NOT NULL,
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
    sample_id INTEGER NOT NULL,
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
    sample_id INTEGER NOT NULL,
    created TIMESTAMP NOT NULL,
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
    sample_id INTEGER NOT NULL,
    created TIMESTAMP NOT NULL,
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