import sys

N,m,M,T,R = map(int, sys.stdin.readline().split())

X = m
time = 0
cnt = 0

if m + T > M:
    print(-1)
    exit()

while cnt < N:
    time += 1
    if X + T <= M:
        X += T
        cnt += 1
    else:
        X = max(m, X - R)
print(time)