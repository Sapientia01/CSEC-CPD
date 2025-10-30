#chala_CSEC_hiko

n = int(input())
a = "I hate it"
b = "I love it"
c = "I hate that"
d = "I love that"
l = []

if n > 1:
    for i in range(n-1 ):
        if i % 2 == 0:
            l.append(c)
        else:
            l.append(d)  
    if n % 2 == 0:
        l.append(b)
    else:
        l.append(a) 
else:
    print(a)

print(" ".join(l))