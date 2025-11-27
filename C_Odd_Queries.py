t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    nums = list(map(int,input().split()))

    prefix_sum = [0 for i in range(n+1)]
    cur_sum = 0

    for i in range(n):
        cur_sum += nums[i]
        prefix_sum[i+1] = cur_sum

    for i in range(m):
        l,r,k = map(int, input().split())

        left = prefix_sum[l-1] -prefix_sum[0]
        right = prefix_sum[-1] - prefix_sum[r]

        num = left + (k * (r-l+1)) + right

        # print(left)
        # print(right)
        # print(k * (r-l+1))
        # print(num)
        if num % 2 == 0:
            print("NO")
        else:
            print("YES")



