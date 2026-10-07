text = "  Welcome to IMCC!  "

print("Remove Spaces", text.strip())

print("Lower Case : ", text.lower())

print("Upper Case : ", text.upper())

print("Captilize First Letter : ", text.capitalize())

print(text.title())

print("Letter C occurs : ", text.count("C"), "times in text")

print("Position of IMCC in text is ", text.find("IMCC"))

print(text.replace("IMCC", "Python Magic"))

print(text.startswith("  We"))
print(text.endswith("!  "))

#10. Split string into list by a delimiter
print("Simple Split", text.split())

#11. Join a list of strings with a seprator
words = ["Python", "is", "fun"]
print(" ".join(words))


#