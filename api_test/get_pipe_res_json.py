import sys
import requests

'''
python get_pipe_res_json.py pipe_res.word PQC.xls
'''

word_file = sys.argv[1]

word_list = []
with open(word_file, 'r') as wf:
    for line in wf.readlines():
        each = line.strip("\n").split(' ')
        word_list.append(each)

res_list = []
res_file = sys.argv[2]
with open(res_file, 'r') as rf:
    rf.readline()
    for line in rf.readlines():
        each = line.strip("\n").split('\t')
        res_list.append(each)

def generate_json(res_l, word_l):
    json_res = {"project_name": "ChinaMAP-phase1", "cluster_name": "CNGB"}
    for index, word in enumerate(word_l):
        if res_l[index] == 'NA':
            continue
        elif word[1]  == 'Float':
            json_res[word[0]] = float(res_l[index])
        elif word[1]  == 'Integer':
            json_res[word[0]] = int(res_l[index])
        else:
            json_res[word[0]] = res_l[index]
    return json_res

res_json = []
for res in res_list:
    res_json.append(generate_json(res, word_list[3:]))

#print(res_json[2])


r = requests.post("http://127.0.0.1:5000/pipe_upload", json=res_json)
print(r.text)