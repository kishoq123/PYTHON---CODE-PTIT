import math
t = int(input())

def nto(n):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def check(n):
    cnt = 0
    for i in range(len(n)):
        cnt += int(n[i])
        if i % 2 == 0 and int(n[i]) % 2 !=0:
            return False
        elif i % 2!=0 and int(n[i]) % 2 ==0:
            return False
    if nto(cnt) == False:
        return False
    else:
        return True
    
for i in range(t):
    n = input()
    if check(n):
        print("YES")
    else:
        print("NO")