import math
t = int(input())

def nto(s):
    if s < 2: return False
    for i in range(2,int(math.sqrt(s)) + 1):
        if s % i == 0: return False
    return True

for i in range(t):
    n = input()
    cnt=0
    check = "YES"
    if nto(len(n)):
        for j in range(len(n)):
            if nto(int(n[j])):
                cnt+=1
        if cnt < int(len(n)/2):
            check = "NO"
    else:
        check = "NO"
    print(check)    