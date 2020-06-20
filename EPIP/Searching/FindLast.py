def findLast(arr, target):
    left, right, result = 0, len(arr) - 1, -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if target < arr[mid]:
            right = mid - 1

        elif target == arr[mid]:
            left = mid + 1
            result = mid

        else:
            left = mid + 1

    return result
            