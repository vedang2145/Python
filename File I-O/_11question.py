# Write a program to read a text from certificate.txt and
#  find whether it contains the word 'live'.

f = open("certificate.txt","r")
data = f.read()

data = data.lower()

if "live" in data:
  print("'Live' word is present ")
else:
  print("'Live' word is not present")  
