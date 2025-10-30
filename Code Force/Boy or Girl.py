username = input()
characters = set(username)
if len(characters) % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')
