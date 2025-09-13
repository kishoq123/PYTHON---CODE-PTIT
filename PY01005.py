import math

n = input()
ans=0
for i in range(len(n)):
    if n[i] == '4' or n[i] == '7':
        ans+=1
if ans == 4 or ans == 7:
    print('YES')
else:
    print('NO')