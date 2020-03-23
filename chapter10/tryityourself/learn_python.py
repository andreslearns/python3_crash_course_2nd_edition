#View a content of a txt file

print ("\nVIEWING THE CONTENT OF A FILE")
with open ('learn.txt') as file_object:
    file = file_object.read()
print (file.rstrip())

#loops
print ("\nVIEWING THE CONTENT VIA LOOPS")

with open ('learn.txt') as file_object:
    for f in file_object:
        print (f.rstrip())



print ("\nSTORING THE LINES IN A LIST")
with open('learn.txt') as file_object:
    file = file_object.readlines()

files = ''
for line in file:
    files += line
#print (f"{files.strip()}")
print (files.replace('python', 'C'))