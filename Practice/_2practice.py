# Biggest Number.

number1 = int(input("Enter the first Number : "))
number2 = int(input("Enter the second Number : "))
number3 = int(input("Enter the third Number : "))

if (number1 > number2 and number1 > number3):
  print(number1 ,"is big")
elif(number2 > number3):
  print(number2, "is big")
else:
  print(number3, "is big")    
