N,K = map(int,input().split())

def bfs():
    queue = [N]
    visited = [0]*100001
    while queue:
        x = queue.pop(0)
        if x == K:
            return visited[x]
        for nx in (x-1,x+1,x*2):
            if 0<=nx<100001 and not visited[nx]:
                visited[nx] = visited[x]+1
                queue.append(nx)

print(bfs())