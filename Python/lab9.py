dict1 = {}
dict1["hostname"] = "R1"
dict1["mgmt-ip"] = "10.1.1.1"
dict1["username"] = "Joson"
dict1["password"] = "cisco"

dict2 = {}
dict2["hostname"] = "R2"
dict2["mgmt-ip"] = "10.1.1.2"
dict2["username"] = "Joson"
dict2["password"] = "cisco"

interface_r1 = {}
interface_r1 ["interface"] = "G1"
interface_r1 ["ip-address"] = "192.168.1.1"

interface_r2 = {}
interface_r2 ["interface"] = "G1"
interface_r2 ["ip-address"] = "192.168.1.2"

datacenter = [dict1, dict2]

datacenter[0]["interface"] = interface_r1
datacenter[1]["interface"] = interface_r2

import json

print(json.dumps(datacenter, indent=4))