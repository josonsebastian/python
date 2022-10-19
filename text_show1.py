from netmiko import ConnectHandler
import textfsm
import json

r1 = ConnectHandler(ip="192.168.122.70", username="cisco", password="cisco", device_type="cisco_ios")
r2 = ConnectHandler(ip="192.168.10.2", username="cisco", password="cisco", device_type="cisco_ios")

devices = [r1, r2]

def get_show(dev):
	hostname = dev.send_command("sh run | in hostname").split()[1]
	showrun = dev.send_command("sh cdp neighbors")
	with open('cisco_ios_show_cdp_neighbors.textfsm') as temp:
		fsm = textfsm.TextFSM(temp)
		output = fsm.ParseText(showrun)

	print("Hostname :" + hostname)
	print(fsm.header)
	print(output)

for device in devices:
	get_show(device)
	print("\n*************************\n")
	device.disconnect()


