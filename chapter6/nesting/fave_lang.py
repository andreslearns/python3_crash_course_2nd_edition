favorite_languages = {
    'jen': ['python','ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskel']
}
#looping with the key values in the first for loop
for name, languages in favorite_languages.items():
    print (f"{name.title()}'s favorite languages are:")
    #then we loop to get the value of the list inside the dict.
    for language in languages:
        print (f"\t{language.title()}")