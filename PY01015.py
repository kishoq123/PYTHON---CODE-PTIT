t = int(input())

for i in range(t):
    ok = True
    n = input()
    for j in range(1,len(n)):
        if n[j-1] > n[j]:
            ok = False
            break
    if ok:
        print('YES')
    else :
        print('NO')