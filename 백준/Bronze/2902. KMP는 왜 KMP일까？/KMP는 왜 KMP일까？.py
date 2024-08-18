name = input()

name = name.split('-')
for i in name:
    print(i[0], end='')
