w,h = map(int,input().split())
a,h1 = map(int,input().split())
b,h2 = map(int,input().split())

snow_weight = w

for i in range(h,-1,-1):
   snow_weight += i
   if i == h1:  
    snow_weight -= a
   if i == h2: 
    snow_weight -= b
   if snow_weight < 0:
     snow_weight = 0
print(snow_weight)     