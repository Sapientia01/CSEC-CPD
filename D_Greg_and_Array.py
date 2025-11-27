n,m, k =  list( map(int, input().split()))
nums = list( map(int, input().split()))
opr = []
op_count = [0 for i in range(m+1)]
total_addition = [0 for i in range(n+1)]

for _ in range(m):
    opr.append(list( map(int, input().split())))

for i in range(k):
    a,b =  list( map(int, input().split()))
    op_count[a] += 1
    if b  < m:
        op_count[b+1] -= 1


cur_opr = 0
for i,o in enumerate(op_count):
    cur_opr += o
    op_count[i] = cur_opr


for i,o in enumerate(op_count[1:]):
    l,r,d = opr[i]

    total_addition[l] += (o * d)
    if r < n:
        total_addition[r+1] -= (o * d)


cur_add = 0
for i,o in enumerate(total_addition):
    cur_add += o
    total_addition[i] = cur_add


for i,o in enumerate(total_addition[1:]):
    nums[i] += total_addition[i+1]


print(*nums)

