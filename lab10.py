vlans = [{"id": "10", "name": "data"}, {"id": "20", "name": "voice"}, {"id": "30", "name": "mgmt"}]

with open("newvlan.cfg", "w") as modify_vlans:
    modify_vlans.write("vlan " + vlans[0]["id"] + "\n")
    modify_vlans.write("vlan " + vlans[0]["name"] + "\n")
    modify_vlans.write("vlan " + vlans[1]["id"] + "\n")
    modify_vlans.write("vlan " + vlans[1]["name"] + "\n")
    modify_vlans.write("vlan " + vlans[2]["id"] + "\n")
    modify_vlans.write("vlan " + vlans[2]["name"] + "\n")


import os

os.chdir("/home/jo/Desktop/Python")

os.sytem("cat newvlan.cfg")



vlans = [{"id": "10", "name": "data"}, {"id": "20", "name": "voice"}, {"id": "30", "name": "mgmt"}]
modify_vlans = open("vlans.cfg", "w")
modify_vlans.write("vlan " + vlans[0]["id"] + "\n")
modify_vlans.write("vlan " + vlans[0]["name"] + "\n")
modify_vlans.write("vlan " + vlans[1]["id"] + "\n")
modify_vlans.write("vlan " + vlans[1]["name"] + "\n")
modify_vlans.write("vlan " + vlans[2]["id"] + "\n")
modify_vlans.write("vlan " + vlans[2]["name"] + "\n")

modify_vlans.close()

import os

os.chdir("/home/jo/Desktop/Python")

os.sytem("cat newvlan.cfg")

