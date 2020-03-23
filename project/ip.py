from netaddr import valid_ipv4

ip = input("enter ip address : ")
if valid_ipv4(ip):
    print ("valid")
else:
    print ("not valid")