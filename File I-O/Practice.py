#Q1

# f = open("names.txt","r")

# names = []

# for i in f:
#   names.append(i.strip())
# print(names)  

#Q2

# f = open("names.txt","r")

# for i in f:
#   name = i.strip()

#   if len(name) > 5:
#     print(name)  

#Q3

f = open("names.txt","r")
count = 0
for i in f:
  name = i.strip()
  if name[0].lower() in "aeiou":
    count = count + 1
print(count)     