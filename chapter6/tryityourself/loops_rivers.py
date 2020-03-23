rivers = {'nile': 'egypt','pasig': 'philippines', 'shinano': 'japan'}

for k, v in rivers.items():
    print(f"The {k.title()} river is located to {v.title()}")

print ('-' * 40)
for k in rivers.keys():
    print (f"Most Beutiful rivers in the world is: {k.title()}")
    
print ('-' * 40)

for v in rivers.values():
    print (f"Most Beautiful country in the world is: {v.title()}")