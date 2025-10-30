k,n,w = [int(i) for i in input().split()]
s = 0
for i in range(w):
    x = i +1
    s += k * x
if s > n:
    print(s-n)
else :
    print(0)
