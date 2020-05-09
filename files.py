# Python has functions for creating, reading, updating and deleting files.

# Open a file
myFile = open('myfile.txt', 'w')

# Get some info
print('Name : ', myFile.name)

print('Opening Mode : ', myFile.mode)

# Write to file
myFile.write('I love python')
myFile.write('an JavaScript')
myFile.close()
print('Is Closed : ', myFile.closed)

# Append to file
myFile = open('myfile.txt', 'a')
myFile.write(' I also like Ruby')
myFile.close()

# Read from a file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)