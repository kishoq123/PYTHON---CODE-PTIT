import math
t = int(input())

for i in range(t):
    s = input()
    check = True
    for j in range(len(s)):
        if(s[j] != '4' and s[j] != '7'):
            check = False
            break
    if check:
        print('YES') 
    else :
        print('NO')       