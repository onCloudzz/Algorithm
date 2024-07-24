from sys import stdin

N,M = map(int,stdin.readline().split())

cards = list(map(int,stdin.readline().split()))

max = 0

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if cards[i]+cards[j]+cards[k] > max and cards[i]+cards[j]+cards[k] <= M:
                max = cards[i]+cards[j]+cards[k]
print(max)