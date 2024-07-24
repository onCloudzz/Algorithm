from sys import stdin

N = int(stdin.readline())

S = [0]*20

for _ in range(N):
    inputs = list(map(str, stdin.readline().split()))
    if len(inputs) == 1:
        a = inputs[0]
    else:
        a, b = inputs

    if a == "add":
        b = int(b)-1
        S[int(b)] = 1
    elif a == "remove":
        b = int(b)-1
        S[int(b)] = 0
    elif a == "check":
        b = int(b)-1
        print(S[int(b)])
    elif a == "toggle":
        b = int(b)-1
        S[int(b)] = 1 - S[int(b)]
    elif a == "all":
        S = [1]*20
    elif a == "empty":
        S = [0]*20