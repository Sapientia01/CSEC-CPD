# n,m = map(int, input().split())
# s = input()
# c = set(s)
# a = 0
# b = 0
# l = []
# for i in c:
#     x = s.count(i)
#     if x >= m :
#         print(0)
#         print(s)
#         break
#     else:
#         pass
#     if x > a:
#         a = x
#         b = i
#         l.clear()
#         y = (b,a)
#         l.append(l)
# print(l)


# hiko_chala_CSEC_ICPC_B

n, k = map(int, input().split())
s = list(input().strip())
best_cost = float('inf')
best_num = None
best_d = -1

for d in range(10):
    current_d = str(d)
    count = s.count(current_d)
    if count >= k:
        current_cost = 0
        candidate = s.copy()
    else:
        required = k - count
        candidates = []
        for idx, c in enumerate(s):
            if c != current_d:
                c_int = int(c)
                cost = abs(c_int - d)
                candidates.append((cost, c_int, idx))
        
        def sort_key(item):
            cost, c, idx = item
            if c > d:
                group = 0
                pos_key = idx
            else:
                group = 1
                pos_key = -idx
            return (cost, group, pos_key)
        
        candidates.sort(key=sort_key)
        if len(candidates) < required:
            continue  # This case is impossible per problem constraints
        
        selected = candidates[:required]
        current_cost = sum(item[0] for item in selected)
        candidate = s.copy()
        for item in selected:
            _, _, idx = item
            candidate[idx] = str(d)
    
    if current_cost < best_cost or (current_cost == best_cost and d < best_d):
        best_cost = current_cost
        best_d = d
        best_num = candidate

print(best_cost)
print(''.join(best_num))