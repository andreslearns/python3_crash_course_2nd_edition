filename = 'pi_digits.txt'


with open(filename) as fileobject:
    lines = fileobject.readlines()

pi_string = ''

for line in lines:
    pi_string += line.strip()

birthday = input("Enter Your Bithday in the form of MMDDYY: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print ("Your birthday does NOT appear in the first million of pi!")

print (len(pi_string))