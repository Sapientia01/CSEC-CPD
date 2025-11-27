n,m = map(int, input().split())
nums = list(map(int,input().split()))


l_to_r = [0 for i in range(n)]
r_to_l = [0 for i in range(n)]

up = 0
down = 0

for i in range(n-1):
    if nums[i+1] < nums[i]:
        up += (nums[i] - nums[i+1])
        l_to_r[i+1] = up
        r_to_l[i+1] = down
    elif nums[i+1] > nums[i]:
        down +=  (nums[i+1] - nums[i])
        r_to_l[i+1] = down
        l_to_r[i+1] = up
    else:
        l_to_r[i+1] = up
        r_to_l[i+1] = down
        


for _ in range(m):
    l,r = map(int, input().split())
    if r > l :
        print(l_to_r[r-1] - l_to_r[l-1])
    else:
        print(r_to_l[l-1] - r_to_l[r-1])
        