#2.Create a heterogenous list of numbers and names.
#  Split the list from highest number.

list1 = [20, "Raj", 23, "Amit", 50, "Neha", 35]

highest = 50
i = list1.index(highest)

print(list1[:i])
print(list1[i:])

