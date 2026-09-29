from ncclient import manager
from xml.dom import minidom

my_device = {
        "host": "192.168.184.230",
        "port": 830,
        "username": "admin",
        "password": "admin",
        "hostkey_verify": False
}

my_filter = """
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
  </interfaces>
  """

with manager.connect(**my_device) as connection:
    result = connection.get_config(source="running", filter=("subtree", my_filter)).xml
    print(minidom.parseString(result).toprettyxml())