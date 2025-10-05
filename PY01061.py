import math

def nto(n):
    if n < 2: 
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0: return False
    return True

def check(n):
    if nto(int(n[-3::])) and nto(int(n[:3])):
        return True
    return False
    

t = int(input())

for i in range(t):
    n = input()
    if check(n):
        print("YES")
    else:
        print("NO")
        