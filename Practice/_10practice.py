# Square of even numbers using List.

number = [1,2,3,4,5,6,7,8]
result = []

for i in number:
    if i % 2 == 0:
        result.append(i * i)
print(result)