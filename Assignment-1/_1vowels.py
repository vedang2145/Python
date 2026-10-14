# 1.Write a program to read a file and 
# count how many vowels are present in its content.

file = open("assignment.txt","r")

count = 0
content = file.read()

for ch in content:
  if ch.lower() in "aeiou":
    count = count + 1

file.close()

print("Vowels = ", count)
