ip_adress = "10.1.5.5"
interface = "Gi0/0/0/0"
list = [interface, ip_adress, "Configuerd by Python", "shut"]
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list)
list[3] = "no shut"
print("IP address of the router", list[1], "management interface", list[0]) 

