import requests
import json
import sys
import yaml
import pdb


response = requests.get("http://api.open-notify.org/astros.json")
print(response.status_code)
print(response.json())
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())

parameters = {
    "lat": 40.71,
    "lon": -74
}
print("******************************************")
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

jprint(response.json())

pass_times = response.json()['request']
jprint(pass_times)

yaml.dump(response.json, allow_unicode=True)
