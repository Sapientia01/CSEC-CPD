n = int(input())
coins = list(map(int,input().split()))
coins.sort()

total_coins = sum(coins)


min_num = 0
grater_sum = 0

for i in range(n):
    if grater_sum <= total_coins/2:
        grater_sum += coins[n-i-1]
        min_num += 1

print(min_num)        

