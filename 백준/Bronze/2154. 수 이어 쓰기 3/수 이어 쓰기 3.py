nums = ""
N = int(input())

for i in range(1, N+1):
    nums += str(i)

print(nums.index(str(N))+1)