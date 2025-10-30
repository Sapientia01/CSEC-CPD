# nums = [3,1,2,2,2,1,3]
# k = 2
nums = [1,2,3,4]
k = 1

p= 0
for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        if nums[i] == nums[j] and (i*j) %2 == 0:
            p+= 1

print(p)