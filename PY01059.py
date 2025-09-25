t = int(input())

for i in range(t):
    n = input()
    chan = 0
    le = 1
    check = False
    for i in range(len(n)):
        if i % 2 == 0:
            chan += int(n[i])
        elif i % 2 != 0 and int(n[i]) != 0:
            le *= int(n[i])
            if int(n[i]) == 1:
                check = True
    if check == False and le == 1:
        le = 0
    print(chan, end=' ')
    print(le)
print()
