ip_address = "10.1.5.5"
temp_ip_address = ip_address.replace("5", "2")
print(temp_ip_address)
new_ip_address = temp_ip_address.replace("2", "100", 1)
csr_ip_address = "Gateway IP {}"
print(csr_ip_address.format(new_ip_address))
