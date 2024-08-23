N = input()

original = ""
current_digit = 0

for i in range(1,1000000):
    original += str(i)
    for j in range(len(str(i))):
        if str(i)[j] == N[current_digit]:
            current_digit += 1
            if current_digit == len(N):
                print(i)
                exit()