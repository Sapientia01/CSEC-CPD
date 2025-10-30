t = int(input())
for _ in range(t):
    n,k = list(map(int,input().split()))
    nums = list(map(int,list(input())))
    one_window = sum(nums[0:k])
    ans = "YES"
    if one_window >= k:
        ans = "NO"

    for i in range(n-k):
        one_window = one_window - nums[i] + nums[i+k]
        if one_window >= k:
            ans = "NO"
            break

    
    print(ans)

    if ans == "YES":
        res = [0 for i  in range(n)]
        x = 1
        y = n
        for i in range(n):
            # print(i)
            # print(n)
            if nums[i] == 0:
                res[i] = y 
                y -= 1
            else:
                res[i] = x
                x += 1
        
        print(*res)




































































