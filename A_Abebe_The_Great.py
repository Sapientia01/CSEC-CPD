#chala_CSEC_hiko

a = input()
b = input()
out = ""
for i in range(len(a)):
    if a[i] == b[i]:
        out += '0'
    else:
          out += '1'  
print(out)