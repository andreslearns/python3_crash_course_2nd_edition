rental_cars = {
    'subaru' : {'color': 'blue', 'model': 2019},
    'mitsubishi': {'color': 'black', 'model': 2017},
    'toyota': {'color': 'black', 'model': 2017}
}
prompt = input (f"Select a brand of car: subaru/fortuner/mitsubihi: ")

for brand, info in rental_cars.items():

    if brand == prompt:
        print (f"\nSorry {brand.title()} is not available")
    elif prompt not in brand:
        print (f'No cars available!')
    else:
        print (f" {brand.title()} is the only available")
        print (f"\tcolor: {info['color']}")
        print (f"\tmodel: {info['model']}")
#        print (info)
        