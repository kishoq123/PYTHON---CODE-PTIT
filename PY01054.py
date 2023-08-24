import math

def check(n):
    cnt = 1
    for i in range(len(n)):
        if int(n[i]) != 0:
            cnt *= int(n[i])
    return cnt
    
t = int(input())
for i in range(t):
    n = input()
    print(check(n))
print()
        
