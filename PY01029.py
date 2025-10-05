import math
t = int(input())

for i in range(t):
    n = input()
    m = ''.join(reversed(n))
    a = int(n)
    b= int(m)
    if math.gcd(a,b) == 1:
        print('YES')
    else :
        print('NO')