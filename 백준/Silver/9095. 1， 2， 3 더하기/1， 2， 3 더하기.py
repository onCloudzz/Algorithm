from sys import stdin

n = int(stdin.readline())

for _ in range(n):
    m = int(stdin.readline())
    dp = [0] * (m + 1)
    dp[0] = 1
    for i in range(1, m + 1):
        for j in range(1, 4):
            if i - j >= 0:
                dp[i] += dp[i - j]
    print(dp[m])