from netmiko import ConnectHandler
from rich import print

my_device = {
    "device_type": "cisco_ios",
    "host": "192.168.184.230",
    "username": "admin",
    "password": "admin"
}

with ConnectHandler(**my_device) as connection:
    version = connection.send_command(command_string="show version", use_genie=True)
    print(version)