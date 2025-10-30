from collections import Counter,defaultdict
for _ in range(int(input())):
    n,k=map(int,input().split())
    arr=input().split()
    c=Counter(arr)
    if any(i%k for i in c.values()):
        print(0)
        continue
    d=defaultdict(int)
    i=j=ans=0
    while i<n and j<=i:
        while d[arr[i]]>=c[arr[i]]//k:
            d[arr[j]]-=1
            j+=1
        d[arr[i]]+=1
        i+=1
        ans+=(i-j)
    print(ans)
    


# from collections import Counter
# for _ in range(int(input())):
#     ans = 0
#     n,k = list(map(int,input().split()))
#     nums = list(map(int,input().split()))
#     counter = Counter(nums)
#     multiset = {}
#     multiset_l = []
#     for key in counter.keys():
#         if counter[key] % k != 0:
#             ans = 0
#             break
#         else:
#             multiset[key] = counter[key] // k
#             multiset_l.extend([key for i in range(counter[key] // k)])


#     window = {}
#     left = 0
#     right = 0
#     while right < n and left < n:


    


    
    
    
    
    
    
    
    
#     print(multiset)
#     print(multiset_l)





















# # from collections import Counter

# # t = int(input())
# # for _ in range(t):
#     # n,k = list(map(int,input().split()))
#     # nums = list(map(int,input().split()))
