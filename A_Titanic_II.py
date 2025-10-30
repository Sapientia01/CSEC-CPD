#hiko_chala_ICPC_B
m = [ "January", 'February', 'March','April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
a = input().capitalize()
n = int(input())
x = m.index(a)
l = (x + n) % 12
print(m[l])
