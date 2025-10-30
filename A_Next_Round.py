n,k = [int(i) for i in input().split()]
l = [int(i) for i in input().split()]
l.sort()
l.reverse()
a = l[k-1]
nr = [i for i in l if i >= a and i> 0]
print(len(nr))