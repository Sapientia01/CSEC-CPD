t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    min_num = nums[0]
    max_num = nums[0]

    for i in nums:
        if i > max_num:
            max_num = i
        if i < min_num:
            min_num = i

    print(max_num-min_num) 