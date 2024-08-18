import sys

def get_table(pattern):
    lenp = len(pattern)
    table = [0] * lenp
    j = 0
    for i in range(1, lenp):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    return table

def KMP(word, pattern):
    table = get_table(pattern)
    lenw = len(word)
    lenp = len(pattern)
    j = 0
    checked = []
    for i in range(lenw):
        while j > 0 and word[i] != pattern[j]:
            j = table[j - 1]
        if word[i] == pattern[j]:
            if j == lenp - 1:
                checked.append(i - lenp + 2)
                j = table[j]
            else:
                j += 1
    return checked

word = sys.stdin.readline().rstrip()
pattern = sys.stdin.readline().rstrip()

checked = KMP(word, pattern)

print(len(checked))
print(*checked)