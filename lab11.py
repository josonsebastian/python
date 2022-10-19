import os

os.chdir("/home/jo/Desktop/Python")


intf = [{"int": "Interface", "name": "G0/0"}, {"int": "Interface", "name": "G0/1"}, {"int": "Interface", "name": "G0/2"}, {"desc": "Description", "name": "Connected via Python"}, {"cmd": "no", "status": "shut"}]

with open("r1.interface.cfg", "w") as modify_intf:
	modify_intf.write(intf[0]["int"] + " " + intf[0]["name"] +"\n")
	modify_intf.write(intf[3]["desc"] + " " + intf[3]["name"] +"\n")
	modify_intf.write(intf[4]["cmd"] + " " + intf[4]["status"] +"\n")
	modify_intf.write(intf[1]["int"] + " " + intf[1]["name"] +"\n")
	modify_intf.write(intf[3]["desc"] + " " + intf[3]["name"] +"\n")
	modify_intf.write(intf[4]["cmd"] + " " + intf[4]["status"] +"\n")
	modify_intf.write(intf[2]["int"] + " " + intf[2]["name"] +"\n")
	modify_intf.write(intf[3]["desc"] + " " + intf[3]["name"] +"\n")
	modify_intf.write(intf[4]["cmd"] + " " + intf[4]["status"] +"\n")


	
r1temp = open("r1.interface.cfg", "r")
R1 = r1temp.read()
print(R1)
	
	