favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
#looping only to the key: with a keyword keys
#Looping through the keys is actually the default behavior when looping
#through a dictionary
friends = ['phil','sarah']
for name in favorite_language.keys():
    print (name.title())
    
    if name in friends:
        language = favorite_language[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
 ##########################################################################       
    if 'erin' not in favorite_language.keys():
        print (f'\nErin please take our poll\n')
        

for name in sorted(favorite_language.keys()):
    print (f"{name.title()}, Thank you for taking the poll.")

print (f"\nThe following languages have been mentioned\n")
for language in favorite_language.values():
    print (language.title())


