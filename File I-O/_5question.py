# with open("practice.txt","w") as file:
#   file.write("Hi everyone \nwe are learning File I/O" \
#   " \nusing java \nI like programming in Java.")

with open("practice.txt","r") as file:
  data = file.read()

new_data = data.replace("java","Python")
print(new_data)  