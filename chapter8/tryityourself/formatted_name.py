def get_fomatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = (f"{first_name} {last_name}")
    return full_name.title()

#musician = get_fomatted_name('jimi','hendrix')
#print (musician)


def get_fomatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_fomatted_name ('andrew', 'soltes')
print (musician)
musician = get_fomatted_name ('Andrew', 'ibarrientos', 'soltes')
print (musician)

