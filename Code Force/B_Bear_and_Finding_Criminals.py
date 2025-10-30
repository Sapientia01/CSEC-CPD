cities , position = list(map(int, input().split()))
criminals = list(map(int,input().split()))
cought = 0
cought += criminals[position-1]

if cities > 1:
    maxPair = min(position-1, cities- position)
    for i in range(1,maxPair+1):
        if criminals[position-1-i] + criminals[position-1+i] == 2:
            cought += 2
    if not(cities % 2 == 1 and position  == cities//2 +1):       
        if position <= cities//2:
                cought += sum(criminals[maxPair*2+1:cities])
        else:
                cought += sum(criminals[0:cities-maxPair*2-1])


print(cought)
