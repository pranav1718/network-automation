import requests
from rich import print

requests.packages.urllib3.disable_warnings()
headers = {"Accept": "application/yang-data+json"}
url = "https://192.168.1.111/restconf/data/Cisco-IOS-XE-native:native/ntp"

result = requests.get(url=url, headers=headers, auth=("admin", "admin"), verify=False)
print(result.text)