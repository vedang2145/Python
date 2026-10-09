#3.Accept the name and check if its palindrome

number = (input("Enter The Number : "))

if number == number[::-1]:
  print("The Number is Palindrome")
else:
  print("The Number is Not Palindrome")  