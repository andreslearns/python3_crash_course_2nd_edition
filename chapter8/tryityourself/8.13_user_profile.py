def build_profile(first, last, **info):
    """ Will make a user profile """
    info ['first_name'] = first
    info ['last_name'] = last
    
    print (f"\nPersonal Information:")
    for key, value in info.items():
        print (f"\t{key.title()} : {value.title()}")


build_profile ('andrew', 'soltes', age='28', location='manila')
build_profile ('ayie', 'plata', age='28', location='manila', middle_name = 'ebora')
