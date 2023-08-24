import math
t = int(input())

def nto(s):
    if s < 2: return False
    for i in range(2,int(math.sqrt(s)) + 1):
        if s % i == 0: return False
    return True

for i in range(t):
    n = input()
    if nto(int(n[-4::])): 
        print("YES")
    else:
        print("NO")
    