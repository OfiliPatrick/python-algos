def convertBinToDec(binary):
    dec = 0
    i = 0
    while binary !=0 :
        last_digit = binary % 10
        part = last_digit *  pow(2,i)
        i+=1
        binary = binary //10
        dec += part

    return dec