#4. Read a file, split its content into words, and store them in a list.
# (1) Print the total number of words
# (2) Print all unique words

file = open("assignment.txt", "r")

content = file.read()
words = content.split()

print("Total words = ", len(words))

unique = set(words)
print("Unique words = ", unique)

file.close()