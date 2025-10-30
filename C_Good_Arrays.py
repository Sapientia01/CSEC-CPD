t = int(input())
for _ in range(t):
    n =  int(input())
    nums = list(map(int,input().split()))
    ans = "NO"
    ones = nums.count(1)
    

    if  n > 1  and sum(nums) >= ones + n :
        ans = "YES"


    print(ans)

