t = int(input())

def check(n):
    if len(n) % 2 == 0:
        return False
    elif n[0] == n[1] or n[0] != n[len(n)-1]:
        return False
    for i in range(2,len(n),2):
        if n[i-2] != n[i]:
            return False
    return True

for i in range(t):
    n = input()
    if check(n):
        print("YES")
    else :
        print("NO")
        