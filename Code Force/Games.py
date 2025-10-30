n = int(input())
team1 = []
team2 = []
g = 0
for i in range(n):
    a,b = [int(i) for i in input().split()]
    team1.append(a)
    team2.append(b)
for x in team1:
    for y in team2:
        if x == y:
            g += 1
print(g)
