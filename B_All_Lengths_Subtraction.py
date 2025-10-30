t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))

    if max(nums) > n or max(nums) < n:
        print("NO")
        continue
    
    left = 0
    right = 0

    while nums[right] != n:
        right += 1

    left = right


    res = "YES"
    cur_num = n

    while left > 0 or right < n-1:
        
        if left > 0  and nums[left-1] + 1 == cur_num:
            left -= 1
            cur_num = nums[left]
        
        elif right < n-1 and nums[right+1] + 1 == cur_num:
            right += 1
            cur_num = nums[right]

        else   :
            res = "NO"
            break

    print(res)





