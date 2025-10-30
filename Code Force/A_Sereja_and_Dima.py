n = int(input())
cards = list(map(int, input().split()))
i = 0
j = n-1

first_player = 0
second_player = 0

step = 0


for x in range(n) :
    card  = max(cards[i], cards[j])
    if x % 2 == 0:
        first_player += card
    else:
        second_player += card
    if cards[i] > cards[j]:
        i += 1
    else:
        j-=1

print(first_player,second_player)        