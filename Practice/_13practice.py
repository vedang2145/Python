# Count Lines

f = open("story.txt","r")
count = 0
for i in f:
    count = count + 1

print("Total Lines = ",count)