def runLengthEncod(s):
    out = ''
    curr_let = s[0]
    cnt = 0
    for i,let in enumerate(s):
        if let == curr_let:
            cnt += 1
        if let != curr_let or i == len(s)-1:      
            out += str(cnt) + curr_let
            cnt = 1
            curr_let = let

    return out

def runLengthDecod(s):
    out = ''
    for i in range(0, len(s), 2):
        factor = s[i]
        letter = s[i + 1]
        out+= (letter * int(factor))

    return out

print(runLengthDecod('4a1b3c2a'))
print(runLengthEncod('aaaabcccaa'))