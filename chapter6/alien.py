alien_0 = {'color':'green', 'points':5}

print (alien_0['color'])
print (alien_0['points'])

##############################################
new_points = alien_0['points']
print (f"You just earned {new_points} points!")


#Adding New Key-Value Pairs in dictionaries

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print (alien_0)

##############################################
#adding to an empty dictionary

alien_0 = {}

alien_0 ['color'] = 'green'
alien_0 ['points'] = 5

print (alien_0)

##############################################
#Modifying Values in a Dictionary 

alien_0 = {'color': 'green'}
print (f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print (f"The alien is {alien_0['color']}.")

##############################################
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print (f"original alien position {alien_0['x_position']}.")

if alien_0 ['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #this must be a fast alien
    x_increment = 3
    #the new position is the old position plust the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment
    
print(f"New position: {alien_0['x_position']}")

#############################################
#removing key-value pairs

alien_0 = {'color': 'green', 'points': 5}
print (alien_0)

del alien_0['points']
print (alien_0)

#############################################
# will make an error
alien_0 = {'color': 'green', 'speed': 'slow'}
print (alien['points'])




