favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for name, language in favorite_language.items():
    print (f"{name.title()} favorite language is\t: {language.title()}")

coders = ['phil', 'andrew', 'ayie', 'ener', 'rollie', 'sarah']
##############################################################################################

print ('-' * 30 )
for coder in coders:
    if coder in favorite_language.keys():
        print (f"Thank you for taking the poll {coder.title()}")
    else:
        print (f"What's you favorite language {coder.title()}?")
