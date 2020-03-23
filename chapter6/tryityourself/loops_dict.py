colors_glossary = {'black': 'itim', 'brown': 'kayumanggi', 'gray': 'kulay abo', 'orange': 'kahel'}

#loops using key-pair value
for english, tagalog in colors_glossary.items():
    print (f"\nEnglish\t: {english.title()}")
    print (f"Tagalog\t: {tagalog.title()}")

print ('_' * 20)
colors_glossary['green'] = 'berde'

#loops using keys
for english in colors_glossary.keys():
    print (f"\ncolors in english\t:{english.title()}")
    
#adding additional colors in dict
colors_glossary ['yellow'] = 'dilawan'
colors_glossary ['purple'] = 'lila'

#deleting key-pair value in list
del colors_glossary['brown']
#loops using values
print ('_' * 20)
for tagalog in colors_glossary.values():
    print (f"kulay sa tagalog\t:{tagalog.title()}")