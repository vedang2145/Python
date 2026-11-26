# Factorial

def fact(number):
    fact = 1

    for i in range(number,0,-1):
        fact = fact * i
    return fact    
print("factorial : ",fact(5))    