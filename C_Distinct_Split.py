t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    
    prefix = [0] * n
    suffix = [0] * n
    
    seen = set()
    for i in range(n):
        seen.add(s[i])
        prefix[i] = len(seen)
    
    seen.clear()
    for i in range(n - 1, -1, -1):
        seen.add(s[i])
        suffix[i] = len(seen)
    
    max_s = 0
    for i in range(n - 1):
        max_s = max(max_s, prefix[i] + suffix[i + 1])
    
    print(max_s)




# t = int(input())
# for _ in range(t):
#     n = int(input())
#     s = input()
#     sa = list(s[0:n-1])
#     sb = set(s[-1])
#     max_s = 0

#     for i in range(n-2,0,-1):
#         cur = s[i]
#         if cur in s[0:i-1]:
#             sb.add(sa.pop())


#         a = len(sa)
#         b = len(sb)
#         if a + b > max_s:
#             max_s = a+b



#     print(max_s)




# t = int(input())
# for _ in range(t):
#     n = int(input())
#     s = input()
#     max_s = 0

#     for i in range(1,n):
#         a = len(set(s[0:i]))
#         b = len(set(s[i:n]))
#         if a + b > max_s:
#             max_s = a+b



#     print(max_s)







# from collections import Counter
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     s = input()
#     freq = Counter(s)
#     max_s = 0

#     for num in freq.values():
#         if num >= 2:
#             max_s += 2
#         else:
#             max_s += 1
#     print(max_s)
