a, k, n = [int(x) for x in input().split()]

b = k - a%k + a
ok =-1

for i in range(b, n+1, k):
    ok = 1
    print(i - a, end = ' ')
if ok ==-1: print(ok)