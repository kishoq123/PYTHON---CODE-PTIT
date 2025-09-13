from itertools import permutations

n = input()

permutations_list = list(permutations(n))

for perm in permutations_list:
    for i in perm:
        print (i, end = '')
    print()