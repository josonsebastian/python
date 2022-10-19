from netmiko import ConnectHandler
import re

r1 = ConnectHandler(ip="192.168.122.70", username="cisco", password="cisco", device_type="cisco_ios")
r2 = ConnectHandler(ip="192.168.10.2", username="cisco", password="cisco", device_type="cisco_ios")

devices=[r1,r2]

def get_hostname(dev):
	hostname = dev.send_command("sh run | in hostname").split()[1]
	print("Hostname :" + hostname)

def get_version(dev):
	output = dev.send_command("sh version")
	pattern = re.compile(r"Version (\S+)")
	version = pattern.search(output)
	print("Version : " + version.group(1))

def get_interface(dev):
	output = dev.send_command("sh run")
	pattern = re.compile(r"interface (\w+\d.\d)\r?\n?\s? ip address ([\d\.]+) ([\d\.]+)")
	match = pattern.findall(output)
	for matches in match:
		print("Interface : " + matches[0] + "\n" + "IP Address : " + matches[1] + " Mask : " + matches[2] + "\n")
	pattern1 = re.compile(r"interface (\w+\d)\r?\n?\s? ip address ([\d\.]+) ([\d\.]+)")
	match1 = pattern1.findall(output)
	for matches in match1:
		print("Interface : " + matches[0] + "\n" + "IP Address : " + matches[1] + " Mask : " + matches[2] + "\n")

for device in devices:
	print("********************\n")
	get_hostname(device)
	print("\n*******************\n")
	get_version(device)
	print("\n*******************\n")
	get_interface(device)
	device.disconnect()
