n,k = map(int,input().split())
arr = list(map(int,input().split()))
cnt = 0
for i in range(n-1,0,-1): #n-1 to 1 리스트를 n-1까지 비교하기
    for j in range(i): #0 to i 0~ i 까지 비교해서
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
            cnt += 1
            if cnt == k:
                print(*arr)
if cnt < k:
    print(-1)