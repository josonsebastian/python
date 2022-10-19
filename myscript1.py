from netmiko import ConnectHandler
import getpass
import readline

rtr_ip = input("Enter the Router IP: ") 
uname = input("Enter Username: ")
passwd = getpass.getpass("Enter Password: ")
command = input("Enter the command to execute: ")

rtr = ConnectHandler(ip=rtr_ip, username=uname, password=passwd, device_type="cisco_ios")

output = rtr.send_command(command)

print(output)

rtr.disconnect()

