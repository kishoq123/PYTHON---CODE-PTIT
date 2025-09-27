t = int(input())

for i in range(t):
    ans = {}
    n = input()
    cr = n[0]
    for j in range(1,len(n)):
        if n[j] >= '1' and n[j] <= '9':
            print(cr*int(n[j]), end='')
        else: 
            cr = n[j]
    print()