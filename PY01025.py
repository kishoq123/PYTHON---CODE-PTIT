n = input()
ans = ''
k=-2
for i in range(len(n)):
    ans = n[-i - 1] + ans
    if k % 3 == 0 : ans = ',' + ans
    k+=1
print(ans.strip(','))