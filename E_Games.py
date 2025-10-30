t = int(input())
home = []
guest = []
max_num = 0

for i in range(t):
    h, g = map(int,input().split())
    home.append(h)
    guest.append(g)

for uniform in guest:
    max_num+=  home.count(uniform)  

print(max_num)      

