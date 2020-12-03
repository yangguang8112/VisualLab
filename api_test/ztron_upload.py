import requests

json_data = [
    {
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
        "chip_name" : "V000000002" ,
        "makeload_operator" : 1 ,
        "makeload_date" : "2020-12-01 01:02:03" ,
        "makeload_beizhu" : "test" ,
        "machine_id" : 1 ,
        "lane_id" : 1 ,
        "seq_type" : "wgs" ,
        "seq_operator" : 2 ,
        "seq_date" : "2020-12-2 01:02:03" ,
        "seq_beizhu" : "test" ,        
    }
]

r = requests.post("http://127.0.0.1:5000/ztron_upload", json=json_data)

print(r.text)
