filename = 'programming.txt'

with open(filename, 'w') as file_object:
	file_object.write("I love progrmming.\n")
	file_object.write("I love creating new games.\n")

with open(filename, 'a') as file_object:
	file_object.write("I also love finding meaning in large datasets.\n")
	file_object.write("I love creating apps that can run in a browser.\n")

filename = 'programming.txt'
with open(filename) as file_object:
	lines = file_object.readlines()
for line in lines:
	print(line.strip())
