t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    found = False
    index = 0
    uniq = nums[0]

    first_nums = list(set(nums[:3]))

    if len(first_nums) == 2:
        for i in first_nums:
            count = nums[:3].count(i)
            if count == 1:
                index = nums.index(i)    




    else:
        for i, num in enumerate(nums):
            if num != uniq:
                index = i
                break

    print(index+1)           