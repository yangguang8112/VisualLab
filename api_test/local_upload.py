#!coding=utf-8
import requests

json_data = [
    {
        "sample_info":{
            "sample_origin_code" : "测试test0001" ,
            "sample_code" : "s00000001" ,
            "sample_dr_count" : 1 ,
            "sample_origin_conc" : 0.2 ,
            "zhijian_ban_code" : "test_zhijian_01" ,
            "zhijian_kongwei" : "test_kongwei_01" ,
            "library_kit_code" : "test_lib_kit_01" ,
            "library_ban_code" : "test_lib_ban_01" ,
            "library_kongwei" : "test_lib_kongwei_01" ,
            "library_name" : "lib_01" ,
            "barcode" : "barcode_01" ,
            "adapter_conc" : 0.12 ,
            "library_conc" : 0.123 ,
            "library_vol" : 1.22 ,
            "out_library_date" : "2020-11-30 01:02:03" ,
            "jianku_beizhu" : "test" ,
            "shangji_kit_code" : "shangji_kit_01" ,
            "DNB_dr_count" : 0.001 ,
            "DNB_name" : "DNB_01" ,
            "DNB_conc" : 0.121 ,
            "chip_name" : "V000000101" ,
            "makeload_operator" : "operator01" ,
            "makeload_date" : "2020-12-01 01:02:03" ,
            "makeload_beizhu" : "test" ,
            "machine_code" : "R000000001" ,
            "lane_id" : "L01" ,
            "seq_type" : "wgs" ,
            "seq_operator" : "operator02" ,
            "seq_date" : "2020-12-2 01:02:03" ,
            "seq_beizhu" : "test" ,
        },
        "raw_data":{
            "xiaji_date" : "2020-12-3 10:02:11",
            "split_rate" : 0.4,
            "esr" : 0.2,
            "basenun_G" : 1022,
            "GC" : 0.8,
            "Q30_read1" : 0.33,
            "Q30_read2" : 0.22,
            "Q30_total" : 0.76,
            "Q20" : 0.122,
            "totalreads_M" : 2837,
            "Lag1" : 0.223,
            "Lag2" : 0.221,
            "Lag_table" : "{\"cycle\":[1,2,3], \"Lag1\":[0.12,0.13,0.14], \"Lag2\":[0.12,0.13,0.14]}",
            "Runon1" : 82.29,
            "Runon2" : 82.29,
            "Runon_table" : "{\"cycle\":[1,2,3], \"Runon1\":[0.12,0.13,0.14], \"Runon2\":[0.12,0.13,0.14]}",
            "cycle_N_max" : 82736,
            "Error_rate_est" : 0.211,
            "ChipProductivity" : 82.22,
            "ImageAre" : 9.22,
            "Offset_table" : "{\"cycle\":[1,2,3], \"X\":[0.12,0.13,0.14], \"Y\":[0.12,0.13,0.14]}",
            "RecoverValue_A" : 0.2,
            "RecoverValue_G" : 0.3,
            "RecoverValue_C" : 0.4,
            "RecoverValue_T" : 0.5,
            "RecoverValue_AVG" : 0.6,
            "RecoverValue_AGCT_table" : "{\"cycle\":[1,2,3], \"A\":[0.12,0.13,0.14], \"G\":[0.12,0.13,0.14]}",
            "Intensity_of_All_DNB_table" : "{\"cycle\":[1,2,3], \"DNB1\":[0.12,0.13,0.14], \"DNB2\":[0.12,0.13,0.14]}",
            "RHO_Intensity_table" : "{\"cycle\":[1,2,3], \"RHO\":[0.12,0.13,0.14]}",
            "Background_Intensity_table" : "{\"cycle\":[1,2,3], \"Background\":[0.12,0.13,0.14]}",
            "SNR_table" : "{\"cycle\":[1,2,3], \"SNR\":[0.12,0.13,0.14]}",
            "BIC" : 0.231,
            "FIT" : 0.221,
            "BIC_table" : "{\"cycle\":[1,2,3], \"BIC\":[0.12,0.13,0.14]}",
            "FIT_table" : "{\"cycle\":[1,2,3], \"FIT\":[0.12,0.13,0.14]}",
        }        
    }
]

r = requests.post("http://127.0.0.1:5000/ztron_upload", json=json_data)

print(r.text)
