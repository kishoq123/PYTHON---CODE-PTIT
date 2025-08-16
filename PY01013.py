import math

def nto(s):
    if s < 2: return False
    for i in range(2,int(math.sqrt(s))+1):
        if s % i == 0: return False
    return True
t = int(input())

for i in range(t):
    k=0
    a, b = [int(x) for x in input().split()]
    ucln = math.gcd(a, b)
    while ucln > 0:
        k += ucln % 10
        ucln = int(ucln/10) 
    if nto(k):
        print("YES")
    else :
        print("NO")