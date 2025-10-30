t  =int(input())
def factorial(n):
    if n== 1 or n == 0:
        return 1
    else:
        return n * factorial( n-1)    


for i in range(t):
    n = int(input())
    tri = 4 *n -2
    nd = tri/2
    p = factorial(n)
    print(int(p))

