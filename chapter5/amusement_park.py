age = 13

if age <= 4:
    print ("Your admission cost is 0PHP")
elif age < 18:
    print ("Your admission cost is 25PHP")
else:
    print ("Your admission cost is 40PHP")
    
##################################################
#much better solution

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print (f"Your admission cost is ${price}.")


###################################################
#Using multiple elif blocks
#You can add elif block as you like
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
    
print (f"Your admission price is ${price}")

####################################################
#omiting else in if-elif chain
#else is not required in if-elif chain

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"Your admission cost is ${price}.")