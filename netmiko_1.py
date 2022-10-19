
import os
from netmiko import ConnectHandler
os.chdir("/home/jo/Desktop/Python/")

print("Connecting to R1")

r1=ConnectHandler(ip="192.168.122.71", username="cisco", password="cisco", secret="cisco", device_type="cisco_ios")
r1.send_command("write")
r1.send_command("terminal length 0")
r1_config=r1.send_command("sh run")
with open ("R1.cfg", "w") as temp:
	temp.write(r1_config)

r1.disconnect()

print("Connecting to R2")

r2=ConnectHandler(ip="192.168.122.72", username="cisco", password="cisco", secret="cisco", device_type="cisco_ios")
r2.send_command("write")
r2.send_command("terminal length 0")
r2_config=r2.send_command("sh run")
with open ("R2.cfg", "w") as temp:
	temp.write(r2_config)

r2.disconnect()


