def redixSort(list,max_digits):
    bins =[[] for i in range(10)]
    final_digit = True

    for num in list:
        digitNum =  (num//max_digits)%10
        if digitNum > 0 and final_digit == True:
              final_digit = False 
        bins[digitNum].append(num)
    list = []

    for bin in bins:
        list.extend(bin)
    bins =[[] for i in range(10)]


    if final_digit == True:
         return list
    else:
         return redixSort(list,max_digits*10)





nums = [12,334,22,44,3467,33,556,234,65667777,333456789,12398507,87592222222]


print(redixSort(nums,1))
