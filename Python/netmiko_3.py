import os
from netmiko import ConnectHandler
os.chdir("/home/jo/Desktop/Python/")

r1=ConnectHandler(ip="192.168.122.71", username="cisco", password="cisco", secret="cisco", device_type="cisco_ios")
r2=ConnectHandler(ip="192.168.122.72", username="cisco", password="cisco", secret="cisco", device_type="cisco_ios")

devices=[r1,r2, fw1]

def devices_config(dev)
	dev.establish_connection()
	hostname=dev.send_command("sh run | inc hostname").split()[1]
	if fw1 in hostname():
		dev.send_command("terminal page 0")
	else:
		dev.send_command("terminal length 0")

	dev.send_command("write")
	shrun=dev.send_command("sh run")
	with open(f"{hostname}.cfg", "w") as devfile:
		devfile.write(shrun)
	dev.disconnect()

for temp in devices:
	devices_config(temp)





