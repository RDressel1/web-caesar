def alphabet_position(letter):
    l_alpha = "abcdefghijklmnopqrstuvwxyz"
    u_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if (letter in l_alpha):
        return l_alpha.index(letter)
    if (letter in u_alpha):
        return u_alpha.index(letter)

def rotate_character(char,rot):
    l_alpha = "abcdefghijklmnopqrstuvwxyz"
    u_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if (char not in l_alpha and char not in u_alpha):
        return char
    position = (rot + alphabet_position(char)) % 26
    if (char in l_alpha):
        return l_alpha[position]
    if (char in u_alpha):
        return u_alpha[position]

def encrypt(text,rot):
    position = 0
    output_string = ""
    while(position < len(text)):
        newchar = rotate_character(text[position],rot)
        output_string = output_string + newchar
        position = position + 1
    return output_string
