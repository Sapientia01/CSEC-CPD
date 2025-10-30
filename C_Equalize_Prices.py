t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    prices = sorted(list(set(map(int,input().split()))))
    # print(price)
    lower = prices[0]
    upper = prices[-1]
    low_max =  prices[0] +k
    up_max = prices[-1]+k

    max_price = low_max
    if(lower+k < upper -k ):
        print(-1)
        continue
    if low_max > up_max:
        max_price = up_max
    print(max_price)
       



    