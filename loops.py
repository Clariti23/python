# A loop is used to iterate over a sequence - a list, a tuple, a dictionary, a set, or a string.

people = ['John', 'Peter', 'Rick', 'Mary']

# Simple for loop
# for person in people:
#     print(f'Current person: {person}')

# Break
# for person in people:
#     if person == 'Rick': break
#     print(f'Current person: {person}')

# Continue
# for person in people:
#     if person == 'Rick': continue
#     print(f'Current person: {person}')

# Range - similar to for loop
# for i in range(len(people)):
#     print(people[i])

# for i in range(0, 11):
#     print(f'Number: {i}') => This prints 0 to 10

# While loops execute as long as initial condition is true.

count = 0
while count <= 10:
    print(f'Count: {count}')
    count += 1