from sys import stdin

N, M = map(int, stdin.readline().split())
castle = [stdin.readline().strip() for _ in range(N)]
row = [0] * N
col = [0] * M
for i in range(N):
    for j in range(M):
        if castle[i][j] == 'X':
            row[i] = 1
            col[j] = 1
print(max(N - sum(row), M - sum(col)))