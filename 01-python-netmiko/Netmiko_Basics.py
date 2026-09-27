from netmiko import ConnectHandler

my_device = {
    "device_type": "cisco_ios",
    "host": "192.168.184.230",
    "username": "admin",
    "password": "admin"
}

my_commands = ["show version", "show run | section hostname", "show run"]
with ConnectHandler(**my_device) as connection:
    for command in my_commands:
        result = connection.send_command(command_string=command)
        print(result)