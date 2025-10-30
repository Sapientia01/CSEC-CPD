# import math

# t = int(input())
# for _ in range(t):
#     a,b = map(int,input().split())
#     max_sum = 0
#     for i in range(1, int(math.sqrt(b)) + 1):
#         if b % i == 0:
#             num1  = (b // i) + (a * i) 
#             num2  = (b // (b // i)) + (a * (b // i)) 
#             if num1 % 2 == 0:
#                 if num1 > max_sum :
#                     max_sum = num1
#             if num2 % 2 == 0:
#                 if num2 > max_sum :
#                     max_sum = num2

#     if max_sum == 0:
#         print(-1)
#     else:
#         print(max_sum)

# import math

# t = int(input())
# for _ in range(t):
#     a, b = map(int, input().split())
#     max_sum = -1

#     for i in range(1, int(math.isqrt(b)) + 1):
#         if b % i == 0:
     
#             k1 = i
#             s1 = a * k1 + b // k1
#             if s1 % 2 == 0:
#                 max_sum = max(max_sum, s1)

     
#             k2 = b // i
#             s2 = a * k2 + b // k2
#             if s2 % 2 == 0:
#                 max_sum = max(max_sum, s2)

#     print(max_sum)



import math

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    max_sum = -1
    
    # iterate over divisors up to sqrt(b)
    for i in range(1, int(math.isqrt(b)) + 1):
        if b % i == 0:
            # divisor i
            s1 = a * i + b // i
            if s1 % 2 == 0:
                max_sum = max(max_sum, s1)
            
            # divisor b // i
            j = b // i
            s2 = a * j + b // j
            if s2 % 2 == 0:
                max_sum = max(max_sum, s2)
    
    print(max_sum)
