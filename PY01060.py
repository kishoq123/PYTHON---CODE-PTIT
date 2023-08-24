t = int(input())

for i in range(t):
    n = input()
    chan = 1
    le = 0
    for i in range(len(n)):
        if i % 2 == 0 and int(n[i]) != 0:
            chan *= int(n[i])
        elif i % 2 != 0:
            le += int(n[i])
    print(chan, end=' ')
    print(le)
print()
