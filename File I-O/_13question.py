# Count the number of lines in a file.

with open("new.txt","r") as f:
  data = f.readlines()
  print(len(data))