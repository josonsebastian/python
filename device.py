
def device_info(temp):
  dev1 = {"hostname": "R1", "OS": "IOS-XE", "mgmt-ip": "10.1.1.1"}
  dev2 = {"hostname": "R2", "OS": "IOS-XR", "mgmt-ip": "10.1.1.2"}
  dev3 = {"hostname": "R3", "OS": "IOS-XE", "mgmt-ip": "10.1.1.3"}
  dev4 = {"hostname": "R4", "OS": "IOS-XR", "mgmt-ip": "10.1.1.4"}
  dev5 = {"hostname": "R5", "OS": "NEXUS", "mgmt-ip": "10.1.1.5"}
  device_list = [dev1, dev2, dev3, dev4, dev5]
  for list in device_list:
    for key, value in list.items():
        if value == "IOS-XE" and temp == "IOS-XE":
	        print("The management IP of " + list["hostname"] + " running IOS-XE is " + list["mgmt-ip"])
        elif value == "IOS-XR" and temp == "IOS-XR":
            print("The management IP of " + list["hostname"] + " running IOS-XR is " + list["mgmt-ip"])
        elif value == "NEXUS" and temp == "NEXUS":
            print("The management IP of " + list["hostname"] + " running NEXUS is " + list["mgmt-ip"])
        else:
            pass