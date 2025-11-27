n, m = map(int, input().split())
books = list( map(int, input().split()))
max_book = 0
left = 0
right = 1
cur_sum = 0

prefix_sum = [0 for i in range(n+1)]
for i in range(n):
    cur_sum+= books[i]
    prefix_sum[i+1] = cur_sum



while right < n+1:
    cur_sum = prefix_sum[right] - prefix_sum[left]
    if cur_sum <= m:
        max_book = max(right - left, max_book)
        right += 1
        
    else:
        left += 1

print(max_book)
