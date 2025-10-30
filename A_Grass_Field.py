t   = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    c,d = map(int,input().split())
    sum_mat =  a+ b+c +d

    if sum_mat == 4:
        print(2)

    elif sum_mat == 0:
        print(0)
    else:
        print(1)    



