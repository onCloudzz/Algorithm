import sys

n = int(sys.stdin.readline())

cnt = 0

for _ in range(n):
    a = int(sys.stdin.readline())
    if cnt == 0:
        cnt += a
    else:
        cnt += a - 1

print(cnt)