f = open("new.txt","r")
# print(f.read())

print(f.read(5))

print(f.read(5))

print(f.tell())   # tell() shows the current status of pointer.

print(f.seek(0))

print(f.seek(7))   # seek() move the pointer.

print(f.seek(0))

for line in f:
  print(line)
