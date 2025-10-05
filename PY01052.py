import math

def nto(n):
    if n < 2: 
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i ==0:
            return False
    return True

def check(n):
    cnt = 0
    rev = []
    for i in range(len(n)):
        cnt += int(n[i])
    if nto(cnt):
        return True
    else:
        return False
    
t = int(input())
for i in range(t):
    n = input()
    if check(n):
        print("YES")
    else :
        print("NO")     
        
