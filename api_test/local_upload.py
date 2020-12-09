import requests

json_data = [
    {
        "sample_info":{
            "sample_origin_code" : "test0001" ,
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
            "chip_name" : "V000000001" ,
            "makeload_operator" : "operator01" ,
            "makeload_date" : "2020-12-01 01:02:03" ,
            "makeload_beizhu" : "test" ,
            "machine_code" : "R000000001" ,
            "lane_id" : 1 ,
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
            "Q30_read2" : 0.22,
            "Q30_total" : 0.76,
            "Q20" : 0.122,
            "totalreads_M" : 2837,
            "Lag" : 0.223,
            "Runon" : 82.29,
            "cycle_N_max" : 82736,
            "Error_rate_est" : 0.211,
            "ChipProductivity" : 82.22,
            "ImageAre" : 9.22,
            "MaxOffsetX_MaxOffsetY" : 28.2,
            "InitialOffsetX_InitialOffsetY" : 1.223,
            "RecoverValue_A_G_T_C_AVG" : 922.2,
            "Intensity_of_All_DNB" : 102.33,
            "RHO_Intensity" : 222.11,
            "Background_Intensity" : 8888,
            "SNR" : 0.111,
            "BIC" : 0.231,
            "FIT" : 0.221,
        }        
    }
]

r = requests.post("http://127.0.0.1:5000/ztron_upload", json=json_data)

print(r.text)
