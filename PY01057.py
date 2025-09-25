import math

t = int(input())

def nto(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def check(n):
    for i in range(len(n)):
        if nto(i) and nto(int(n[i])) == False:
            return False
        elif nto(i) == False and nto(int(n[i])) == True:
            return False
    return True
        
for i in range(t):
    n = input()
    if check(n):
        print("YES")
    else:
        print("NO")