t = int(input())

for i in range(t):
    n = input()
    check = True
    for j in range(2,len(n)):
        if n[j-2] == n[j - 1] or n[j-2] != n[j]:
            check = False
    if check:
        print("YES")
    else:
        print("NO")