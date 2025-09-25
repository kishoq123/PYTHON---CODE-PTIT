import math

def check(n):
    cnt = 0
    rev = []
    for i in range(len(n)):
        cnt += int(n[i])
    if cnt % 3 == 0:
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
        
