t = int(input())
for _ in range(t):
    n = int(input())
    password = input()
    is_strong = "YES"
    for i in range(n-1):
        if ord(password[i]) > ord(password[i+1]) or ord(password[i]) > 57 and ord(password[i]) < 97 or ord(password[-1]) > 57 and ord(password[-1]) < 97:
            is_strong = "NO"
            break


    print(is_strong)



# print(ord("7"))

# print(chr(64))