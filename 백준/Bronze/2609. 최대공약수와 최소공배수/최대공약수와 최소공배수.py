from sys import stdin

def uclid(a,b):
    while b != 0:
        a,b = b,a%b
    return a

a,b = map(int, stdin.readline().split())

print(uclid(a,b))
print(a*b//uclid(a,b))