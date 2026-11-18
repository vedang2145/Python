# Largest number in a list.

number = []
for i in range(5):
  n = int(input("Enter the number : "))
  number.append(n)

largest = number[0]

for i in number:
  if i > largest:
    largest = i
print("Largest Number = ",largest)    