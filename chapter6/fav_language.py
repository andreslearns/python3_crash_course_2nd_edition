favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

language = favorite_language['sarah'].title()
print (f"Sarah's favorite language is {language}.")


####################################################
#error handling using get() method!
#usually used to handles the error if the key does not exist on the dict.
language = favorite_language.get('Andrew','No language assigned for that user!')
print (language)

for k, v in favorite_language.items():
    print(f"\nname\t\t:{k.title()}")
    print(f"language\t:{v.title()}")
    
    