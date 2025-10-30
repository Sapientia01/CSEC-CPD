max_count = int(input())
nums = list(map(int,list(input())))
left = 0
right = 1
n = len(nums)

max_sub = 0


for i in range(n):
    for j in range(n-i-1):
        if sum(nums[j:i+j]) == max_count:
            max_sub += 1

# if n == 1:


print(max_sub)






























# from collections import defaultdict

# k = int(input())
# s = input().strip()

# count = defaultdict(int)
# count[0] = 1  
# prefix_sum = 0
# result = 0

# for ch in s:
#     if ch == '1':
#         prefix_sum += 1
#     result += count[prefix_sum - k]
#     count[prefix_sum] += 1

# print(result)
