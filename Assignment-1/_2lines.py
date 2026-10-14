#2. Read all lines from a file into a list. 
# Print the total number of lines and display the 2nd and 4th line.

file = open("assignment.txt", "r")

lines = file.readlines()

print("Total Number of Lines : ",len(lines))
print("Second Line : ",lines[1])
print("Fourth Line : ", lines[3])

file.close()

