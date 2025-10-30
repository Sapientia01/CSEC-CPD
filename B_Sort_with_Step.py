t = int(input())
for _ in range(t):
    n,k = list(map(int,input().split()))
    nums =list(map(int,input().split()))
    imposible_pos = []
    for i in range(n):
        num = nums[i]
        if abs(num-(i+1)) % k != 0:
            imposible_pos.append([num,i+1])
    if len(imposible_pos) == 0:
        print(0)
        continue
    elif len(imposible_pos) == 2:
         num1 = imposible_pos[0][0]
         num2 = imposible_pos[1][0]
         index1 = imposible_pos[0][1]
         index2 = imposible_pos[1][1]
         if abs(num1 - index2) % k ==  abs(num2 - index1) % k:
             print(1)
    else:
        print(-1)