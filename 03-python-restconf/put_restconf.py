import requests
from rich import print

requests.packages.urllib3.disable_warnings()
headers = {"Content-Type": "application/yang-data+json"}
url = "https://192.168.1.111/restconf/data/Cisco-IOS-XE-native:native/ntp"
myconfig = {
    'Cisco-IOS-XE-native:ntp': {
        'Cisco-IOS-XE-ntp:server': {
            'server-list': [{'ip-address': '3.3.3.3'}, {'ip-address': '4.4.4.4'}, {'ip-address': '5.5.5.5'}]
        }
    }
}

result = requests.put(url=url, headers=headers, auth=("admin", "admin"), json=myconfig, verify=False)
print(result)