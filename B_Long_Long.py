t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    max_sum = 0
    max_op = 0
    open = False
    for num in nums:

        max_sum += abs(num)
        if num < 0 and not open:
            open = True
        elif num > 0 and open:
            max_op += 1
            open = False

    if open :
        max_op += 1

    print(max_sum,max_op)

