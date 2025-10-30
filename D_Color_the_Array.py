#chala_CSEC_hiko

t = int(input())
for i in range(t):
    n = int(input())
    nl = list(map(int,input().split()))
    nl.sort()
    x = sum(nl)
    if (x %2) == 0 :
        print("YES")
    else:
        a = sum(nl[:(len(nl)//3)]) % 2
        b = sum(nl[(len(nl)//3):]) % 2         
        l = sum(nl[:(len(nl)//2)]) % 2
        r = sum(nl[(len(nl)//2):]) % 2
        if l == r  or a == b:
            print("YES")
        else:
            print("NO")    




   


