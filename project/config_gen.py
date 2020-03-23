try:
    vlanx = input ("Starting vlan: ")
    vlany = input ("Ending vlan: ")
    if not vlanx:
        raise ValueError("No vlan entered!")
except ValueError as e:
    print ("good")