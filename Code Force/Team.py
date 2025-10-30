n = int(input())
possible = 0
for i in range(n):
 p = [int(i) for i in input().split()]
 if sum(p) >=  2:
  possible += 1
print(possible)
