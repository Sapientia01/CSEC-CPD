t = int(input())

for _ in range(t):
    n = int(input())
    s =input()
    min_op = n
    found = False


    chars = list(set(s))

    for char in chars:
        possible = True
        left = 0
        right = n-1
        cur_op = 0


        while left < right:
            if s[left] == s[right]:
                left  += 1
                right -= 1

            elif s[left] == char:
                left += 1
                cur_op += 1

            elif s[right] == char:
                right -= 10
                cur_op += 1

            else:
                possible  = False
                break


        if possible:
            found = True
            min_op = min(cur_op,min_op)


    if found:
        print(min_op)
    else:
        print(-1)
        

