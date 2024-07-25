N = int(input())

dicl = {
    1: 1,
    2: 2
}

def dp(n):
    if n in dicl:
        return dicl[n]
    dicl[n] = dp(n-1) + dp(n-2)
    return dicl[n]

print(dp(N) % 10007)