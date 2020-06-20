def arrEqualIndex(arr):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        diff =  arr[mid] - mid
        
        if diff == 0:
            return mid

        elif diff < 0:
            left = mid + 1
            
        else:
            right = mid - 1
            
    return -1
    

print(arrEqualIndex([-2,0,2,3,6,7,9]))