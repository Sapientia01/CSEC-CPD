t = int(input())
team= 0
for i in range(t):
    if sum(list(map(int,input().split())))>=2:
        team+=1
print(team)        