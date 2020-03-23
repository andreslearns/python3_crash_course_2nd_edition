#counting to 20
for value in range(1, 21):
    print (value)

#One Million:
#millions = 1_000_000
#for million in range(millions):
#    print (million)

#Summing a Million

milyones = [1, 10, 100,1000000, 2000000, 30000000]

minimum = min(milyones)
maximum = max(milyones)
summary = sum(milyones)

print (minimum)
print (maximum)
print (summary)

###########################################
#4-6. Odd Numbers

for odd in range (1, 21, 3):
    print (odd)

#4-7. Threes
for three in range (3, 31, 3):
    print (three)
#4-8. Cubes:
for cube in range (1, 10):
    value = cube ** 3
    print (value)
#4-9. Cube Comprehension:
cubes = [value ** 3 for value in range (1, 10)]
print (cubes)