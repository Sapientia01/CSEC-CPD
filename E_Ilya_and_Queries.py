s = input()
q = int(input())

n = len(s)

prefix_sum = [0 for i in range(n+1)]
cur_sum = 0

for i in range(n-1):
    if s[i] == s[i+1]:
        cur_sum += 1
    prefix_sum[i+1] = cur_sum

# print(prefix_sum)

for _ in range(q):
    l,r = map(int, input().split())
    print(prefix_sum[r-1] - prefix_sum[l-1])










# s = input()
# q = int(input())

# n = len(s)

# prefix_sum = [0 for i in range(n+1)]
# cur_sum = 0

# for i in range(n-1):
#     if s[i] == s[i+1]:
#         cur_sum += 1
#     prefix_sum[i+1] = cur_sum

# print(prefix_sum)

# for _ in range(q):
#     l,r = map(int, input().split())
#     print(prefix_sum[r-1] - prefix_sum[l-1])