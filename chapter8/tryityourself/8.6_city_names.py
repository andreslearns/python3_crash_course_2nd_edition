def city_country(city_name, country):
    """ Will format the city and name """
    cities = f"{city_name.title()}, {country.title()}"
    return cities
 
name_cities = city_country('santiago','chile')
print (name_cities)
name_cities = city_country('manila','philippines')
print (name_cities)
name_cities = city_country('chicago','america')
print (name_cities)