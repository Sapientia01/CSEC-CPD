t = int(input())
for _ in range(t):
    max_sum =  0
    min_opration = 0
    start = 0
    n = int(input())
    nums = list(map(int,input().split()))
    for i in range(n):
        max_sum += abs(nums[i])
        if nums[i] < 0:
            start +=1
        if nums[i]> 0  and start > 0:
            min_opration +=1
            start = 0
    if nums[n-1] < 1 and start > 0:
        min_opration +=1
        
    print(max_sum, min_opration)