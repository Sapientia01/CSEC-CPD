n = int(input())
string = input()
one = ''
zeros = ''


for s in string:
    if s == "n":
        one += "1 "
    if s == "z":
        zeros += "0 "

print(one + zeros)