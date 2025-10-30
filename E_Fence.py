n,k = map(int,input().split())
nums = list(map(int,input().split()))
min_sum = sum(nums[0:k])
prev_sum = sum(nums[0:k])
j = 0

# print(min_sum)


right = k

while right < n:
    cur_sum = prev_sum + nums[right] - nums[right-k]

    if cur_sum < min_sum:
        min_sum = cur_sum

        j = right - k + 1
    
    prev_sum = cur_sum
    right += 1

print(j+1)





    # print(prev_sum, cur_sum,j,right)


