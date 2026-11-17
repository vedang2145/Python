# Count vowels in String.

s = input("Enter the String : ")
count = 0

for i in s:
  if i.lower() in "aeiou":
    count = count + 1
print(count)  
