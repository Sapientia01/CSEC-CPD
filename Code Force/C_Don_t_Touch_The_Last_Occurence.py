#hiko_chala_ICPC_B
n = int(input())
l = [int(i) for i in input().split()]
out =[]
for i in l:
    if (i in out):
        out.remove(i)
        out.append(i)
    elif not(i in out):
        out.append(i)

print(len(out))
print(*out)         