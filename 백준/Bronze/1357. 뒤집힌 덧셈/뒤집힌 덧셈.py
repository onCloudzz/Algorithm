from sys import stdin

X, Y = map(str, stdin.readline().split())

print(int(str(int(X[::-1]) + int(Y[::-1]))[::-1]))