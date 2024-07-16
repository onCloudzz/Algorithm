from sys import stdin

munbin = stdin.readline().strip()

a = [0 for i in range(26)]

for i in range(26):
    a[i] += munbin.count(chr(65+i))

oddcnt = 0

for i in range(26):
    if a[i] % 2 == 1:
        oddcnt += 1
    if oddcnt > 1:
        print("I'm Sorry Hansoo")
        exit()

if oddcnt == 1:
    odd = chr(65+a.index([i for i in a if i % 2 == 1][0]))
    a[a.index([i for i in a if i % 2 == 1][0])] -= 1
else:
    odd = ""

for i in range(26):
    print(chr(65+i)*(a[i]//2), end="")
print(odd, end="")
for i in range(25, -1, -1):
    print(chr(65+i)*(a[i]//2), end="")
print()