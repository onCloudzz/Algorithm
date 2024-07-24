from sys import stdin

N = int(stdin.readline())

paper = [list(map(int, stdin.readline().split())) for _ in range(N)]

white = 0
blue = 0

def cut(x, y, n):
    global white, blue
    color = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != paper[i][j]:
                cut(x, y, n//2)
                cut(x, y+n//2, n//2)
                cut(x+n//2, y, n//2)
                cut(x+n//2, y+n//2, n//2)
                return
    if color == 0:
        white += 1
    else:
        blue += 1

cut(0, 0, N)
print(white)
print(blue)