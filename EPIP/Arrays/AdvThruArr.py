def advArr(arr):
    pos = 0
    num_jumps = arr[pos]
    jumper = 0

    for num in arr:
        if num >= len(arr):
            return True
    if arr[0] == 0:
        return False


    
    

arr = [3,3,1,0,2,0,1]
print(advArr(arr))
 
            
        
    

