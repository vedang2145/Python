f = open("new.txt","w")
f.write("This is Python Programming")
f.close()

f = open("new.txt","r")
print(f.read())