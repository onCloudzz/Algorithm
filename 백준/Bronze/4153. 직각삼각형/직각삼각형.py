from sys import stdin

a,b,c = map(int, stdin.readline().split())

while a != 0 and b != 0 and c != 0:
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print('right')
    else:
        print('wrong')
    a,b,c = map(int, stdin.readline().split())