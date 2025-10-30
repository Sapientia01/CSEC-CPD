
n = 9
k = 3




players = list(range(1,n+1))
i = 0
while len(players) > 1:
    i += (k-1)
    if i >= len(players):
        i %= len(players)
    players.pop(i)
print(players[0])      


