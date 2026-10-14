#3. Take a sentence from the user, split it into words, 
# and store the in a list. Print the longest word.

sentence = input("Enter the Sentence : ")

words = sentence.split()

longest = max(words, key=len)

print("Words list : ", words)
print("Longest Word : ", longest)