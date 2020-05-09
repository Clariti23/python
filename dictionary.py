#A dictionary is a collection that is unordered, changeable and indexed. It does not allow duplicate elements.

# Create dict
person = {'first_name': 'John', 'last_name': 'Fero', 'age': 27}

# Use a constructor
# person2 = dict(first_name='Taylor', last_name="Williams")

# Get a value
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '555-555-5555'

# print(person, type(person))

#Get dict_keys
print(person.keys())

# Get dict_items
print(person.items())

# Copy dict
person3 = person.copy()
person3['city'] = "Charlotte"

# Remove item
del (person['age'])
person.pop('phone')

# Clear
person.clear()

# Get length
print(len(person3))

#List of dict
people = [{'name': 'Jill', 'age': 25}, {'name': 'Taylor', 'age': 33}]

print(people[0]['name'])
