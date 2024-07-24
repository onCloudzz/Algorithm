import sys

N,M = map(int, sys.stdin.readline().split())

lanlist = [0]*N

for i in range(N):
    lanlist[i] = int(sys.stdin.readline())

max = 2**31-1
min = 1

mid = (max+min)//2

while min <= max:
    cnt = 0
    for i in range(N):
        cnt += lanlist[i]//mid
    if cnt >= M:
        min = mid + 1
    else:
        max = mid - 1
    mid = (max+min)//2

print(max)