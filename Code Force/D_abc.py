#hiko_chala_ICPC_B
n = int(input())
out = []
for i in range(n):
    w = input()
    a =  w[0] + w[2] + w[1]
    b =  w[2] + w[1] + w[0] 
    c =  w[1] + w[0] + w[2] 
    if ( w == 'abc'or a == 'abc' or b == 'abc' or c == 'abc'):
        out.append('YES')
    else:
        out.append("NO")
for i in out:
    print(i)