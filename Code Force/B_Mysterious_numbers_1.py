# a,b = input().split()
# c = ''

# out = ''
# if len(a) < len(b):
#     for i in range(len(b)-len(a)):
#         c += '0' 
#     a  = c + a
# elif len(a) > len(b):
#       for i in range(len(a)-len(b)):
#         c += '0'   
#       b  = c+b

# for i in range(len(a)):
#     x = int(a[i])
#     y = int(b[len(b)-1-i])
#     out += str(int(x) + int(y))

# print(out)        












a,b = input().split()

l = list(b)
l.reverse()

b =int( ''.join(l))

print(int(a)+b)       
















