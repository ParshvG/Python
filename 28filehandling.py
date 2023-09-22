#"r" - Read - Default value. Opens a file for reading, error if the file does not exist

#"a" - Append - Opens a file for appending, creates the file if it does not exist

#"w" - Write - Opens a file for writing, creates the file if it does not exist

#"x" - Create - Creates the specified file, returns an error if the file exists

file = open("name.txt", 'r')
print(file.read())

file = open("name.txt", 'a')
print(file.write("hi"))
file = open("name.txt", 'r')
print(file.read())

import os 
os.removedirs("hi")

file = open("name.txt", "x")
file = open("name.txt", "w")
file.write("hi hello parshv i am python expert")
file = open("name.txt", "r")
print(file.read())