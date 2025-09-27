import numpy as np

rows, cols = [int(x) for x in input().split()]
matrix = np.empty((rows, cols), dtype=int)

for i in range(rows):
    matrix[i] = [int(x) for x in input().split()]
ans = 0
         
for i in range(rows):
    for j in range(cols):
        if matrix[i,j] == -1:
            for n in range(i-1,i+2,1):
                for m in range(j-1,j+2,1):
                    if matrix[n,m] >=0:
                        ans += matrix[n,m]   
            
print(ans)



