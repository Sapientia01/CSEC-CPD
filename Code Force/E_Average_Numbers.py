n  = int(input())
nums = list(map(int, input().split()))
k = 0
l = []
sumNum = sum(nums)
for i in range(n):
    avg = (sumNum - nums[i]) // (n-1)
    if avg == nums[i]:
        k += 1
        l.append(str(i+1))
print(k)
if k> 0:
    print(' '.join(l))



