# A tuple is a collection that is ordered and unchangeable. It allows for duplicates.

#Create a tuple
fruits = ('Apples', 'Oranges', 'Grapes')
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

#Single value needs a trailing comma
fruits2 = ('Apples', )

#Get a value
# print(fruits[1])

#Can't change a value
# fruits[0] = "Pies"

#Delete a tuple
del fruits2

#Get the length
# print(len(fruits))

# A set is a collection that is unordered and unindexed. It does not allow duplicates.

fruits_set = {'Apples', 'Oranges', 'Mangoes'}

#Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add("Tomato")

# Remove from set
fruits_set.remove("Tomato")

# Add duplicate
fruits_set.add("Apples")

print(fruits_set)
# Clear set
# fruits_set.clear()

# Delete
# del fruits_set

print(fruits_set)