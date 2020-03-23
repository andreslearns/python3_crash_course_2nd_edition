#looping with the values only
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

print (f"\nThe following languages have been mentioned\n")
for language in favorite_language.values():
 
    print (language.title())
    
#will loop using set() which prevent the values for repeating
print ('-' * 20)
for language in set(favorite_language.values()):
    print (language.title())
    
#You can build a set directly using braces and separating the elements with commas:
print ('-' * 20)
languages = {'python', 'ruby', 'python', 'c'}
print (languages)