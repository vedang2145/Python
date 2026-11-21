# Separate even and odd numbers.

even = []
odd = []

for i in range(5):
    n = int(input("Enter the Number : "))

    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

print("Even Number : ",even)
print("Odd Number : ",odd)            