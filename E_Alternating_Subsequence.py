t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    max_sum = 0

    left = 0
    right= 1
    
    while right < n:
        cur_max = nums[left]


        while right < n and nums[right] * nums[left] > 0:
            if nums[right] > cur_max:
                cur_max = nums[right]

            right+= 1

        max_sum+= cur_max

        left = right



 


    if n > 1:
        print(max_sum)
    else:
        print(nums[0])