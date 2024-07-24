import math 
N = int(input())

cnt = 0

dictnum = {1:0, 2:1, 3:1}

for i in range(4, N+1):
    dictnum[i] = dictnum[i-1] + 1
    if i % 2 == 0:
        dictnum[i] = min(dictnum[i], dictnum[i//2] + 1)
    if i % 3 == 0:
        dictnum[i] = min(dictnum[i], dictnum[i//3] + 1)

cnt = dictnum[N]
print(cnt)