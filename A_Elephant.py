# n = int(input())
# min_step = 0

# min_step += n//5 + n%5//4 + n%5%4//3 + n%5%4%3//2  + n%5%4%3%2

# print(min_step)



s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
# s = "abca"
# s = "aba"
# s = "abc"

used = False
is_palindrome = True

left = 0
right = len(s)-1

while left < right and is_palindrome:
    if s[left] == s[right] :
        left += 1
        right -= 1



    elif  s[left] != s[right]  and not used:
        used = True
        if s[left +1] == s[right] and left + 2 < right-1  and s[left+2] == s[right-1]:
            left += 1

        elif s[left] == s[right-1] and  left + 1 < right-2  and s[left+1] == s[right-2]:
            right -= 1

        elif s[left +1] == s[right] and  not(left + 2 < right-1 ):
            left += 1
        
        elif s[left] == s[right-1] and  not(left + 1 < right-2 ):
            right -= 1


    elif  s[left] != s[right]  and used:
            is_palindrome = False


print( is_palindrome) 