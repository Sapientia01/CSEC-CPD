# t = int(input())
# for i in range(t):
#     w = int(input())
#     p1 = input().split()
#     p2 = input().split()
#     p3 = input().split()
#     a = 0
#     b = 0
#     c = 0   
#     i = 0
#     while i < w:
#         l = p1[i]
#         m = p2[i]
#         n = p3[i]

#         p1p = 3 - (p2.count(l) + p3.count(l))
#         p2p = 3 - (p1.count(m) + p3.count(m))
#         p3p = 3 - (p2.count(n) + p1.count(n))

#         if p1p == 3:    
#              a+= p1p
#         else:
#             a+= p1p-1  
        
#         if p2p == 3:    
#              b+= p2p
#         else:
#             b+= p2p-1

#         if p3p == 3:    
#              c+= p3p
#         else:
#             c+= p3p-1
#         i+=1     

#     print(a,b,c)






t = int(input())  
for _ in range(t):  
    w = int(input())  
    p1 = input().split()  
    p2 = input().split()  
    p3 = input().split()  
    
    freq1 = {}
    freq2 = {}
    freq3 = {}
    for word in p1:  
        freq1[word] = freq1.get(word, 0) + 1
    for word in p2:  
        freq2[word] = freq2.get(word, 0) + 1
    for word in p3:  
        freq3[word] = freq3.get(word, 0) + 1
    a = 0  
    b = 0  
    c = 0  
    for i in range(w):  
        l = p1[i]  
        m = p2[i]  
        n = p3[i]  
   
        p1p = 3 - (freq2.get(l, 0) + freq3.get(l, 0))  
        p2p = 3 - (freq1.get(m, 0) + freq3.get(m, 0))  
        p3p = 3 - (freq2.get(n, 0) + freq1.get(n, 0))  

        if p1p == 3:  
            a += p1p  
        else:
            a += p1p - 1  

        if p2p == 3:  
            b += p2p  
        else:
            b += p2p - 1  

        if p3p == 3:  
            c += p3p  
        else:
            c += p3p - 1  

    print(a, b, c)
    


