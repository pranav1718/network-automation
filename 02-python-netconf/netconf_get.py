from ncclient import manager

my_device = manager.connect(
        host="192.168.184.230",
        port=22,
        timeout=30,
        username="admin",
        password="admin",
        hostkey_verify=False,
)

for capability in my_device.server_capabilities:
    print(capability)

my_device.close_session()