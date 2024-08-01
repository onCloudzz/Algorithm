import sys

while True:
    tree = list(map(int, sys.stdin.readline().split()))

    point = 1

    if tree[0] == 0:
        break

    for i in range(tree[0]):   
        point *= tree[2 * (i) + 1]
        point -= tree[2 * (i) +2]

    print(point)