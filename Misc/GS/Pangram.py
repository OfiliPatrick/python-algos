"""
You have given a string =”This is ram”, you need to find all those letters that are missing in the string out of all 26 a-z letters present in alphabets
"""
import string
def pangram(s):
    out =[]
    
    set_s = set(s)

    for letter in string.ascii_lowercase:
        if letter not in set_s:
            out.append(letter)
    return out

print(pangram("This is ram"))