#5-3. Alien Colors #1:
alien = 'green'

if alien == 'green':
    points = +10

print (f"You have additional {points}")


#5-4. Alien Colors #2
if alien == 'yellow':
    points ='+10 points'
else:
    points = '-10 point'
    
print (f"Your point will be: {points}")

if alien == 'blue':
    print(f"You have shot down an alien color {alien}")
else:
    print (f"You need to shutdown an alien with color {alien}")