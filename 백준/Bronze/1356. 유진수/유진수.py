N = input()

for i in range(1, len(N)):
    aN = list(map(int, N[:i]))
    bN = list(map(int, N[i:]))
    mulA = 1
    for j in aN:
        mulA *= j
    mulB = 1
    for j in bN:
        mulB *= j

    if mulA == mulB:
        print('YES')
        exit()
else:
    print('NO')
