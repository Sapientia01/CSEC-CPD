t = int(input())
def count_letter(word,letter,i):
    l = i
    while(l< len(word) and word[l] == letter):
        l+=1
    return l-i    
for _ in range(t):
    original_sound = input()
    heared_sound = input()
    correct = True
    o_i = 0
    h_i = 0

    while o_i < len(original_sound) and h_i < len(heared_sound):
        O_bits = count_letter(original_sound,original_sound[o_i],o_i)
        h_bits = count_letter(heared_sound,heared_sound[h_i],h_i)
        if h_bits / O_bits < 1 or h_bits / O_bits > 2:
            print("NO")
            correct = False
            break
        else:
            o_i += O_bits
            h_i += h_bits

    if correct == True:
        print("YES")




