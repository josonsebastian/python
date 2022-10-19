import os
from netmiko import ConnectHandler
os.chdir("/home/jo/Desktop/Python/")

r1=ConnectHandler(ip="192.168.122.71", username="cisco", password="cisco", secret="cisco", device_type="cisco_ios")
r2=ConnectHandler(ip="192.168.122.72", username="cisco", password="cisco", secret="cisco", device_type="cisco_ios")

devices=[r1,r2]
n=1

for temp in devices:
	temp.send_command("write")
	temp.send_command("terminal length 0")
	config=temp.send_command("sh run")
	with open ("R" + str(n) + ".cfg", "w") as temp1:
		temp1.write(config)

	n=n+1
	temp.disconnect()





