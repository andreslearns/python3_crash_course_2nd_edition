def build_cars(brand, types, **optional_parts):
    """ we will make a car """
    print(f"\nCar Information:")
    
    optional_parts['brand'] = brand
    optional_parts['types'] = types
    
    for k, v in optional_parts.items():
        print(f"\t{k.title()} \t:  {v.title()}")
        
        
build_cars ('suzuki', 'suv', wheel = 'offroad')
build_cars ('yamaha', 'uv', wheel = 'normal', bumper ='war machine')
build_cars ('bigbee', 'tank', steer = 'metal steer', load = '18', bumper= 'war machine')