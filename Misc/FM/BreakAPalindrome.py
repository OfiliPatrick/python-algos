def breakPal(s):
    if len(set(s)) == 1:
        return "IMPOSSIBLE"

    for index, char in enumerate(s):
        if char != 'a':
            new_string = s[0:index] + 'a' + s[index+1:]
            if not isPalindrome(new_string):
                return new_string

    return "IMPOSSIBLE"
    
def isPalindrome(s):
    first = 0; last = len(s) - 1
    while first < last:
        if s[first] != s[last]:
            return False

        first += 1
        last-=1

    return True


s = 'acca'

print(breakPal(s))