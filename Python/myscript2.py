from netmiko import ConnectHandler
import sys

args = sys.argv
rtr_ip = input("Enter the Router IP: ") 
uname = args[1]
passwd = args[2]
command = input("Enter the command to execute: ")

rtr = ConnectHandler(ip=rtr_ip, username=uname, password=passwd, device_type="cisco_ios")

output = rtr.send_command(command)

print(output)

rtr.disconnect()

