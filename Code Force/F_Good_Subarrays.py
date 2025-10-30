t = int(input())
for i in range(t):
    n = int(input())
    nums = input()
    prefix_sum = [0]*(n+2)
    prev = 0
    good_arr = 0

    for i in range(n):
        prev += int(nums[i])
        prefix_sum[i] = prev
        if int(nums[i]) ==1:
            good_arr +=1 


    for i in range(n):
        for j in range(i+1,n):
            arr_length = j-i + 1
            arr_sum = prefix_sum[j] - prefix_sum[i-1]
            if arr_length == arr_sum:
                good_arr+=1
    print(good_arr )

