N,M = input().split()
N = int(N)
M = int(M)

remind = input()

for i in range(M):
    post = input()
    cnt = 0
    for j in range(len(post)):
        if remind[cnt] == post[j]:
            cnt += 1
        if cnt == len(remind):
            break
    if cnt == N:
        print("true")
    else:
        print("false")