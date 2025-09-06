t = int(input())

for i in range(t):
    n = input()
    check = True
    s=''
    for j in n: s = j + s
    for i in range(1,len(n)):
        if abs(ord(n[i]) - ord(n[i-1])) != abs(ord(s[i]) - ord(s[i-1])):
            check = False
    if check:
        print('YES')
    else:
        print('NO')