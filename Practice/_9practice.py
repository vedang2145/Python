# Count words

f = open("story.txt","r")

content = f.read()
words = content.split()

count = len(words)

print("Total Words = ",count)

f.close()