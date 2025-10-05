from itertools import combinations
a, n = [int(x) for x in input().split()]

arr = {}

k = [int(x) for x in input().split()]
b = [0] * (n+1)

for i in k:
    arr[i] = 1
k = sorted(list(arr))

combination_list = list(combinations(k,n))

for combo in combination_list:
    for i in combo:
        print(i, end=' ')
    print()


