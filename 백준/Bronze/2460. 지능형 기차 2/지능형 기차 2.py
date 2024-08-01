import sys

cnt = 0
max = 0

for _ in range(10):
    a, b = map(int, sys.stdin.readline().split())
    cnt -= a
    cnt += b
    if cnt > max:
        max = cnt

print(max)