print ('x'* 60)
print (f"\t\tSWITCH CONFIG GENERATOR")
officename = input ("OFFICE NAME: ")
functions = input ("ASW or EDSW: ")
print ('x'* 60)
print (f"\t\tSECURITY TEMPLATE")
localuser = input ("USERNAME: ")
localpass = input("PASSWORD: ")





print (f''* 60 + "\n" + "\t\tCOPY AND PASTE IN THE SWITCH")
print ('x'* 60)
print (f"conf t")
print (f"hostname SPARC-{officename.upper()}-{functions.upper()} ")
print (f"username {localuser} privilege 15 secret 5 {localpass}")
