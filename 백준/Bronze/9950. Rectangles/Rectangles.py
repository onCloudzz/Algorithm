from sys import stdin

a,b,c = map(int,stdin.readline().split())

while a != 0 or b != 0 or c != 0:
    if a == 0:
        print(c//b,b,c)
    elif b == 0:
        print(a,c//a,c)
    elif c == 0:
        print(a,b,a*b)
    a,b,c = map(int,stdin.readline().split())