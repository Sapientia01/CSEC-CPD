t = int(input())
for i in range(t):
    n = int(input())
    nums = input()
    prefix_sum = [0]*(n+1)
    prev = 0
    good_arr = 0

    for i in range(n):
        prev += int(nums[i])
        prefix_sum[i+1] = prev

    diction = {}

    for i,num in enumerate(prefix_sum):
        num = int(num) - i
        if num in diction:
            diction[num] += 1
            good_arr+= diction[num] -1
        else: diction[num] = 1


    print(good_arr )