# Cube using lambda 

def lam(n):
    cube = lambda n: n * n * n
    return cube(n)
print("Cube = ",lam(5))