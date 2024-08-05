import sys

N = int(sys.stdin.readline())

platform = [[0]*3 for _ in range(N)]

total = 0

for i in range(N):
    platform[i] = list(map(int, sys.stdin.readline().split()))

platform.sort(key=lambda x: (x[0], x[1]))

max = 0

for i in range(N):
    if platform[i][2] > max:
        max = platform[i][2]

ground = [0] * max

for i in range(N):
    total += ((platform[i][0] - ground[platform[i][1]])+(platform[i][0] - ground[(platform[i][2]-1)]))
    for j in range(platform[i][1], platform[i][2]):
        ground[j] = platform[i][0]
    
    

print(total)