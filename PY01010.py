t = int(input())

for i in range(t):
    n = input()
    s = n[0] + n[1]
    x = n[len(n)-2] + n[len(n)-1]
    if s == x:
        print("YES")
    else:
        print("NO")