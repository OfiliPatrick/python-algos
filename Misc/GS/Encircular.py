def encircular(commands):
    responses = []
   
    for command in commands:
        response = isCircle(command)
        responses.append(response)

    return responses

def isCircle(command):

    if command == "G":
        return 'NO'

    if command == "L" or command == "R":
        return "YES"
    
    directions = {"north" : 0,"east" : 1,"south" : 2,"west" : 3}
    x_cord, y_cord = 0, 0
    
    starting_direction = current_direction = directions["north"]

    for i in range(len(command)):
        command_string = command[i]

        if command_string == "L":
            current_direction = (4 + current_direction - 1) % 4
        
        elif command_string == "R":
            current_direction = (current_direction + 1) % 4
                 
        else:
            if current_direction == directions["north"]:
                y_cord += 1
            if current_direction == directions["east"]:
                x_cord += 1
            if current_direction == directions["south"]:
                y_cord -= 1
            if current_direction == directions["west"]:
                x_cord -= 1
                

    if (x_cord, y_cord) == (0, 0) or starting_direction != current_direction:
        return "YES"

    else:
        return "NO"

print(encircular(['G']))
print(encircular(['L']))
print(encircular(['GRGL']))
    



    

