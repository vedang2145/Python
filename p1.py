# create a list of 10 numbers and display the sum of last 4 elements.

my_list = [1, 4, 7, 3, 9, 7, 0, 2, 5, 8]

total = sum(my_list[-4:])

print(my_list)
print("Sum of last 4 elements:", total)
