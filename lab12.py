from netmiko import ConnectHandler
R1 = ConnectHandler(ip="192.168.122.71", username="cisco", password="cisco", secret="cisco", device_type="cisco_ios")
R1.is_alive()
R1_config = R1.send_config_from_file("R1.cfg")
print(R1_config)
R1.disconnect()
