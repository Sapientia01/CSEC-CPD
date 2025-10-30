t = int(input())
for _ in range(t):
   n,k = list(map(int, input().split()))
   word = input()
   f_req = word[0:k].count("W")
   min_req = word[0:k].count("W")
   if k < n and f_req > 0: 
      for i in range(n-k):
         if word[i] == 'W':
            min_req -= 1
         if word[i+k] == "W":
            min_req += 1
         f_req = min(f_req, min_req)
         

   print(f_req)



















# t = int(input())
# for _ in range(t):
#    n,k = list(map(int, input().split()))
#    word = input()
#    f_req = word[0:k].count("W")
#    min_req = word[0:k].count("W")
#    if k < n and f_req > 0: 
#       for i in range(n-k):
#          if word[i] == 'W' and word[i+k] == "B":
#             min_req -= 1

#    print( min(f_req,min_req) if min(f_req,min_req) > 0 else 0 )
