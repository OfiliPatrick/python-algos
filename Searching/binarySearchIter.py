arr = [1, 2, 3]

def binSearchIter(arr, key):
    first = 0
    last = len(arr) - 1
    while first <= last:
        mid = (first + last) // 2
        if arr[mid] == key:
            return True
        elif key > arr[mid]:
            first = mid+1
        else:
            last = mid -1

    return False
print(binSearchIter(arr, 4))



