n,m = map(int, input().split())
nums = list(map(int,input().split()))
nums.sort()

prefix_sum = [0 for i in range(n+1)]
cur_sum = 0


for i in range(n):
    cur_sum += nums[i]
    prefix_sum[i+1] = cur_sum

# print (prefix_sum)
# print()
# print()
# print()


for _ in range(m):
    x,y = map(int, input().split())

    l = n - x
    r = l + y
    # print(l,r)
    print(prefix_sum[r] - prefix_sum[l]) 




