def AND(a,b):
    if a+b == 2:
        return 1
    else:
        return 0
    
def OR(a,b):
    if a+b == 0:
        return 0
    else:
        return 1

def NOR(a,b):
    c = OR(a,b)
    if c == 1:
        return 0
    else:
        return 1
def NAND(a,b):
    c = AND(a,b)
    if c == 1:
        return 0
    else:
        return 1  

    
      
def twist(c):
    if c == 1:
        return 0
    else:
        return 1    


a  = twist(int(input()))
b  = twist(int(input()))
c  = twist(int(input()))
d  = twist(int(input()))





a1 =  OR(a,b)
b1 = NOR(c,d)                 
c1 = AND(b,c)
d1 = OR(a,d)

a2 = AND(a1,b1)
b2 = NOR(c1,d1)

o = OR(a2,b2)




print(o)




# a1 =  OR(a,b)
# b1 = NOR(c,d)                 
# c1 = AND(b,c)
# d1 = OR(a,d)

# a2 = AND(a1,b1)
# b2 = NOR(c1,d1)

# o = OR(a2,b2)








# a1 =  OR(a,b)
# b1 = AND(c,d)                 
# c1 = AND(b,c)
# d1 = OR(a,d)

# a2 = AND(a1,b1)
# b2 = AND(c1,d1)

# o = OR(a2,b2)
