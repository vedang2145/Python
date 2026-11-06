f = open("new.txt","a")
f.write("\nand I want to learn it.")
f.close()

f = open("new.txt","r")
print(f.read())