import math

def check(n):
    cnt = 0
    rev = []
    for i in range(len(n)):
        cnt += int(n[i])
    if cnt < 10:
        return False
    rev = ''.join(reversed(str(cnt)))
    if int(rev) == cnt: 
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
        
