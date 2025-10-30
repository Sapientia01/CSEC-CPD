#hiko_chala_ICPC_B
l = list(input())
out = ''
if(len(l)) < 7:
    out = "NO"
else:
    for i in range(len(l)-6):
        if (l[i] == l[i+1] == l[i+2]== l[i +3]== l[i+4] == l[i+5] == l[i+6]):
            out = "YES"
        else:
            out = "NO"
        if out == "YES":
            break    
print(out)
