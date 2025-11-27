from bisect import bisect_right

s,b = map(int, input().split())
ships = list( map(int, input().split()))
res = [0 for i in range(s)]
golds = [0 for i in range(b+1)]
cur_sum = 0
query = []

for i in range(b):
    d,g = list(map(int, input().split()))
    query.append([d,g])

query.sort()

for i,q in enumerate(query):
    cur_sum += q[1]
    golds[i+1] = cur_sum



for i,ship in enumerate(ships):
    x = bisect_right(query,[ship,89088])
    res[i] = golds[x]



print(*res)