from math import sqrt

def findDistance(x,y):





t = int(input())
x, y = map(int,input().split())

up = y
down = y
right = x
left = x

for _ in range(t-1):
    x, y = map(int,input().split())
    up = max(up,y)
    down = min(down,y)
    right = max(right,x)
    left = min(left,x)


d = sqrt((up- down)**2 + (right-left)**2)

print(d/2/2)












