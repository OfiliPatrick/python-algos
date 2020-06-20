arr = [1, 2, 3, 4, 5]

key = 9

def search(arr, key, left, right):
    if left > right:
        return False
    mid = (left+right) //2
    if arr[mid] == key:
        return True

    elif key > arr[mid]:
        return (search(arr, key, mid+1, right))
    else:
        return (search(arr, key, left, mid - 1))
        

print(search(arr,key,0, len(arr)-1))
        

    