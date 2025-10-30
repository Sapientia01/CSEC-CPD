#chala_CSEC_hiko
t = int(input())
for i in range(t):
    n = int(input())
    s = list(input().lower())
    sc = s[0]
    for i in range(n):   
          if s[i] != sc[-1]:
               sc += s[i]
    if sc == 'meow' :
          print("YES") 
    else:
         print('NO')
