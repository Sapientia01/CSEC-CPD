n,k = map(int,input().split())
cards = sorted(list(map(int,input().split())))
pairs = []
for i in range(n//3 *2):
    y = cards[i]
    x  = k - y
    cards[i] = ' '
    if x in cards:
        pairs.append([y,x])
        j = cards.index(x)
        cards.pop(j)
    else:
      cards[i] = y
    if i+1 >= len(cards):
        break  
for i in range(cards.count(' ')):
   cards.remove(' ')

if len(cards) > 2:
    for i in range(len(cards)//3 *2 ):
        y = cards[i]
        l = [x for x in cards if x > 0 and  x < k - cards[i]] 
        if len(l) >= 2:
            z = max(l)
            if y + z <= k:
                j = cards.index(z)
                pairs.append([y,z])
                cards.pop(j)
                cards[i] =  -22222222
        if i+1 >= len(cards):
          break            
for i in range(cards.count(-22222222)):
   cards.remove(-22222222)
p = len(cards)//2
i = 0
while i < len(cards):
    pairs.append([cards[i],cards[i+1]])
    i += 2
    # cards.pop(0)
    # cards.pop(0)

firstPlayer = [x[0] for x in pairs ]
secondPlayer = [x[1] for x in pairs]

print(p)
print(' '.join(map(str, firstPlayer )))
print(' '.join(map(str, secondPlayer )))
