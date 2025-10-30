t= int(input())
for _ in range(t):
    n = int(input())

    if n > 45:
        print(-1)
    else:
        num = ""
        x = n
        while x > 0:
            for i in range(9,0,-1):
                if x - i >=  0:
                    num =  str(i) + num
                    x -= i
        num_sum = sum( map(int,num))
        if num_sum == n:
            print(num)
        else:
            print(-1)              



























# t= int(input())
# for _ in range(t):
#     n = int(input())
#     if n <= 10:
#         print(n)
#     elif n > 45:
#         print(-1)
#     else:
#         num = n + 1
#         found = False
#         while num < 987654321:
#             if len(set(str(num))) == len(str(num)):
#                 num_sum = sum( map(int,list(str(num))))
#                 if num_sum == n and num != n:
#                     print(num)
#                     found = True
#                     break
#                 else:
#                     num += 1
#             else:
#                 num += 1
    
#         if not found:
#             print(-1)


# # num = 12
# # while num < 987654321:
# #     num += 1
# #     print(num)