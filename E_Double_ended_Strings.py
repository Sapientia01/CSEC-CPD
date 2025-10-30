t = int(input())

for _ in range(t):
    a = input()
    b = input()
    
    n = len(a)
    m = len(b)
    
    max_common = 0
    

    for i in range(n):
        for j in range(i, n):

            sub_str = a[i:j+1]
            

            if sub_str in b:
                max_common = max(max_common, len(sub_str))



    out = (n - max_common) + (m - max_common)
    print(out)