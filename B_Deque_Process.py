t = int(input())
for i in range(t):
    n = int(input())
    nums = list( map(int, input().split()))
    ans = ''
    r = len(nums)-1
    l = 0
    cur = nums[r]
    up = False


    while l < r:

        if nums[r] > cur and not up:
            cur = nums[r] 
            up = True
            ans += "R"
            r -= 1
        else:
            cur = nums[l]
            up = False
            ans += "L"
            l += 1
            

        
    print(ans)
