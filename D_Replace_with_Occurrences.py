# from collections import Counter

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     b = list(map(int,input().split()))
#     out = ''
#     len = 0
#     total = Counter(b)
#     print(total)
#     x = n
#     for i in total:
#         out+= (str(x) + " ") * i
#         x -= 1
#         len += i
    





#     if len > n :
#         print(-1)
#     else:
#         print(out.strip())


from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    
    pos = defaultdict(list)
    for i, val in enumerate(b):
        pos[val].append(i)
    
    possible = True
    a = [0] * n
    next_val = 1
    
    for k, indices in pos.items():
        if len(indices) % k != 0:
            possible = False
            break
        for i in range(0, len(indices), k):
            for j in range(i, i + k):
                a[indices[j]] = next_val
            next_val += 1
    
    if not possible:
        print(-1)
    else:
        print(" ".join(map(str, a)))

























# t = int(input())
# for _ in range(t):
#     n = int(input())
#     b = list(map(int,input().split()))
#     out = ''
#     len = 0
#     total = list(set(b))
#     x = n
#     for i in total:
#         out+= (str(x) + " ") * i
#         x -= 1
#         len += i

    



#     if len > n :
#         print(-1)
#     else:
#         print(out.strip())


