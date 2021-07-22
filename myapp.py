import requests
import json


URL = "http://localhost:8000/student/"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(URL, data=json_data)
    data = r.json()
    print(data)


get_data(1)
