t= int(input())
for _ in range(t):
    k = int(input())
    num = 0
    x = 0
    i = 0
    

    while i < k:
        num += 1
        if num % 3 != 0 and str(num)[-1] != "3":
            i += 1 
            x = num

    print(x)