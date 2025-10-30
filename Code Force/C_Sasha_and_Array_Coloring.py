t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    i = 0
    j = n-1
    maximum = 0

    while i < j:
        maximum += (nums[j] -nums[i])
        i +=1
        j-=1
    print(maximum)