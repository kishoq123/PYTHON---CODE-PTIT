t = int(input())

for i in range(t):
    check = False
    n = input()
    m =0
    for j in range(1,len(n)):
        if abs(int(n[j-1]) - int(n[j])) == 2:
            m +=int(n[j-1])
            check = True
        else:
            check = False
            break
    m+=int(n[len(n)-1])
    if m % 10 != 0 : check = False
    if check : print("YES")
    else : print("NO")
    