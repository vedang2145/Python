# Sum of all numbers from 1 to N.

number = int(input("Enter the number for sum : "))

count = 0
for i in range(1,number+1):
  count = count + i
print(count)