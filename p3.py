# Print the difference between largest and smallest number in the list.

my_list = [3,8,6,1,7]
print(my_list)

my_list.sort()
print(my_list)

diff = my_list[-1] - my_list[0]
print(diff)