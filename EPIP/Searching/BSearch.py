def binSearch(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return target, mid

        elif target < arr[mid]:
            right = mid - 1
            
        else:
            left = mid + 1
            
    return -1
    

print(binSearch([1,5,5,5,6,7,8,], 5))