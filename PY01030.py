import math 
a, b = [int(x) for x in input().split()]
def check(a,b):
    cnt=1
    for i in range(10**(b-1),10**b-1):
        if math.gcd(a,i) == 1:
            print(i, end=' ')
            if cnt % 10 == 0:
                print()
            cnt+=1
check(a,b)