# Count frequency of each character in string using dictionary.

s = input("Enter the String : ")
frequency = {}

for i in s:
    if i in frequency:
        frequency[i] = frequency[i] + 1
    else:
        frequency[i] = 1

for i in frequency:
    print(i, ":", frequency[i])        
