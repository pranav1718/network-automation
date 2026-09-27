from netmiko import ConnectHandler
from rich import print

my_device = {
    "device_type": "cisco_ios",
    "host": "192.168.184.230",
    "username": "admin",
    "password": "admin"
}

with ConnectHandler(**my_device) as connection:
    interfaces = connection.send_command("show interfaces", use_textfsm=True)
    
    for interface in interfaces:
        # Only print if description is not empty
        if interface.get("description"):
            print(f"[bold green]{interface['interface']}[/bold green]: {interface['description']}")