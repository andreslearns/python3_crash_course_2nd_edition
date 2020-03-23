age = 12


if age <= 2:
    stage = 'baby'
elif age <= 4:
    stage = 'toddler'
elif age <= 13:
    stage = 'kid'
elif age <= 20:
    stage = 'teenager'
else:
    stage = 'elder'

print (f"Your age is {age} and you are a {stage}.")

fruits = ['apple', 'orange', 'mango', 'banana']

if 'apple' in fruits:
    print (f"adding {fruits[0]}")

if 'orange' in fruits:
    print (f"adding {fruits[1]}")
    
if 'mango' in fruits:
    print (f"adding {fruits[2]}")

if 'banana' in fruits:
    print (f"adding {fruits[3]}")

print (f"\nFruits salad ingredients added!")

