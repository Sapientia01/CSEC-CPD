def is_list_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i+1]:
            return False
    return True


t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    pref = list(map(int, input().split()))
    nums = [0 for i in range(k)]
    
    for i in range(k-1,0,-1):
        nums[i] = (pref[i] - pref[i-1])
    nums[0] = pref[0]


    if n == k:
        if  is_list_sorted(nums):
            print("Yes")
        else:
            print("No")
    
    elif k > 1:
        right_first = nums[1]
        left_end = nums[0] / (n-k+1)


        if  is_list_sorted(nums[1:]) and right_first >= left_end:
            print("Yes")
        
        else:
            print("No")
    else:
        print("Yes")
