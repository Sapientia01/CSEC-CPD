t = int(input())
for _ in range(t):
    k,x = map(int,input().split())
    steps = 0
    while steps < k:
        if x  == 4 and k > 1:
            x *= 2 
            steps += 1
        elif (x-1)%3 == 0:
            x = (x-1)//3
            steps += 1
        else:
            x *= 2  
            steps += 1

    print(x)          



