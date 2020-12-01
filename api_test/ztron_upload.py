import requests

json_data = {'sample_id': 100}

r = requests.post("http://127.0.0.1:5000/ztron_upload", json=json_data)

print(r.text)
