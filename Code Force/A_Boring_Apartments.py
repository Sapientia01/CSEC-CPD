t = int(input())
for i in range(t):
    l = input()
    a = int(l[0])
    c = [1,2,3,4]
    x = sum(c) * (a-1) + sum(list(range(len(l)+1)))
    print(x)