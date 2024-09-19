import numpy as np

N = 7
arr = np.zeros((N, N), dtype=int)

for i in range(N):
    for j in range(N):
        arr[i][j] = (j + 1) % 2
        
for row in arr:
    for elem in row:
        print(elem, end=' ')
    print()
