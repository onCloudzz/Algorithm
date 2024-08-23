import sys

while True:
    if (s := sys.stdin.readline().strip()) == "*":
        break
    n = len(s)
    flag = True
    for i in range(n - 1):
        setword = set()
        for j in range(n - i - 1):
            word = setword.add(s[j] + s[j + i + 1])

        if len(setword) != n - i - 1:
            flag = False
            break
    print(f"{s} is{' NOT' if not flag else ''} surprising.")