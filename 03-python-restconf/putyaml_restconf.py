import requests
import yaml
from rich import print

requests.packages.urllib3.disable_warnings()
headers = {"Content-Type": "application/yang-data+json"}


def load_configs():
    myconfig = yaml.safe_load(open("R1.yml"))
    return myconfig

def push_config(myconfig):
    url = "https://192.168.1.111/restconf/data/Cisco-IOS-XE-native:native/ntp"
    result = requests.put(url=url, headers=headers, auth=("admin", "admin"), json=myconfig, verify=False)
    return result


myconfig = load_configs()
result = push_config(myconfig)
print(result)