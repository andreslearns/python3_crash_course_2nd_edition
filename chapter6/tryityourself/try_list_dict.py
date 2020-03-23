#DICTIONARIES INSIDE THE LIST
#6-7. People
filipino = {'username': 'asoltes', 'first': 'andrew', 'last':'soltes'}
american = {"username": 'jsmith','first':'james','last': 'smith'}
chinese =  {'username': 'blee', 'first':'bruce', 'last': 'lee'}


nationality = [filipino, american, chinese]
#print (nationality)

filipino['location'] = 'philippines'
american['location'] = 'america'
chinese['location'] = 'china'

filipino['contact'] = '8888'
american['contact'] = '911'
chinese['contact'] = '119'

for info in nationality:

    print ("\nPersonal information")
    print ('-' * 60)
    print (f"\tusername:\t {info['username']}")
    print (f"\tfullname:\t {info['first'].title()} {info['last'].title()}") 
    print (f"\tlocation:\t {info['location'].title()}")
    print (f"\temergency:\t {info['contact'].title()}")
######################################################################################
dog = {
    
    'type': 'small',
    'breed': 'shih tzu',
    'age': 7,
    'trait': 'playful',
    }

cat = {
    'type': 'big',
    'breed': 'persian cat',
    'age': 9,
    'trait': 'bored as fuck'
    }

dog['owner'] = 'andrew'
dog['name'] = 'tiny and puru'

cat ['owner'] = 'angelo'
cat ['name'] = 'berdugo'


pets = [dog, cat]

print ('-' * 60)
for pet in pets:
    if pet ['owner'] == 'andrew':
        print (f"{pet['owner'].title()} loves dog and he owns a {pet['type'].title()} {pet['breed'].title()} named {pet['name'].title()}")
        print (f"\n{pet['name'].title()} 's additional Information")
        print (f"\t\t{pet['trait'].title()}")
        print (f"\t\t{pet['age']} years old")

        
    else:
        print ('-' * 60)
        print (f"{pet['owner'].title()} loves cat and he owns a {pet['type'].title()} {pet['breed'].title()} named {pet['name'].title()}")
        print (f"\n{pet['name'].title()} 's additional Information")
        print (f"\t\t{pet['trait'].title()}")
        print (f"\t\t{pet['age']} years old")

######################################################################
#6-9. Favorite Places:
print ('-' * 60)

favorite_places = {'andrew': 'sagada', 'ayie': 'baguio', 'brye':'calaguas'}

for name, favorite_place in favorite_places.items():
    print (f"{name.title()} favorite place is {favorite_place.title()}")

######################################################################
print ('-' * 60)
#6-10. Favorite Numbers:
favorite_numbers = {
    'andrew': [30, 14, 69],
    'ayie': [5, 24],
    'brye': [72]
    
}

for name, favorite_number in favorite_numbers.items():
    print (f"{name.title()} favorite number is : {favorite_number} and Total of:{len(favorite_number)} numbers")
    
print ('-' * 60)

######################################################################
#6-11. Cities:

cities = {
    
    'manila'    :  {'country':'philippines', 'abbrev': 'ph', 'population': '82 millions' },
    'new york'  :  {'country': 'america', 'abbrev': 'ny', 'population': '176 millions'},
    'jakarta'   :  {'country':'indonesia', 'abbrev': 'ind', 'population': '560 millions'}
}

for city, info in cities.items():
    print (f"{city.title()} will be found in {info['country'].title()} with abbrev {info['abbrev'].upper()} populations of {info['population']}")
    
    
    