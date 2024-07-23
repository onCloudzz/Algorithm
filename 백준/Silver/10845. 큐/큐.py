from collections import deque
import sys 
N = int(sys.stdin.readline())

queue = deque()

for i in range(N):
    A = sys.stdin.readline().split()

    if A[0][1] == 'u':
        queue.append(A[1])
    elif A[0][1] == 'o':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif A[0][1] == 'i':
        print(len(queue))
    elif A[0][1] == 'm':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif A[0][1] == 'a':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    elif A[0][1] == 'r':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
