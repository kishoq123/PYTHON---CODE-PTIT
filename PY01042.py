t = int(input())

for i in range(t):
    n = input()
    check = True
    for j in range(len(n)):
        if(n[j] != '1' and n[j] != '2' and n[j] != '0'):
            check = False
            break
    if(check):
        print("YES")
    else:
        print("NO")