def robotPos(moves):
    x = 0
    y = 0

    for move in moves:
        if move == 'U':
            y += 1
            
        if move == "D":
            y -= 1
            
        if move == "L":
            x -= 1
            
        if move == "R":
            x += 1

    result = (x,y)  
    return result
    

print(robotPos("UDDLRL"))
print(robotPos("UDDLLRUUUDUURUDDUULLDRRRR"))
            
        
