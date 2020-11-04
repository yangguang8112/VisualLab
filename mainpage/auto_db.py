#from db import get_db
import random


def gener_data(float_count, raw_count):
    data_list = []
    for i in range(raw_count):
        chip_id = 'V' + str(i)
        lane_id = 'L01'
        sample_id = 'S' + str(i)
        created = '2020-11-04'
        tmp = [i, chip_id, lane_id, sample_id, created]
        tmp += [str(round(random.random(),3)) for j in range(float_count)]
        data_list.append(tmp)
    return data_list

raw_data_list = gener_data(23, 1000)
qc_data_list = gener_data(19, 1000)
align_data_list = gener_data(9, 1000)
analy_data_list = gener_data(14, 1000)

#db = get_db()
gener_tool_data = open('gener_tool_data.sql', 'w')
for raw in raw_data_list:
    sql = '''INSERT INTO raw_data VALUES (%d, '%s', '%s', '%s', '%s', %s);''' % (
        raw[0], raw[1], raw[2], raw[3], raw[4], ", ".join(raw[5:])
    )
    gener_tool_data.write(sql + '\n')
    #db.executescript(sql)

for raw in qc_data_list:
    sql = '''INSERT INTO qc_res VALUES (%d, '%s', '%s', '%s', '%s', %s);''' % (
        raw[0], raw[1], raw[2], raw[3], raw[4], ", ".join(raw[5:])
    )
    gener_tool_data.write(sql + '\n')
    #db.executescript(sql)

for raw in align_data_list:
    sql = '''INSERT INTO align_res VALUES (%d, '%s', '%s', '%s', '%s', %s);''' % (
        raw[0], raw[1], raw[2], raw[3], raw[4], ", ".join(raw[5:])
    )
    gener_tool_data.write(sql + '\n')
    #db.executescript(sql)

for raw in analy_data_list:
    sql = '''INSERT INTO analy_res VALUES (%d, '%s', '%s', '%s', '%s', %s);''' % (
        raw[0], raw[1], raw[2], raw[3], raw[4], ", ".join(raw[5:])
    )
    gener_tool_data.write(sql + '\n')
    #db.executescript(sql)

gener_tool_data.close()
#db.close()
