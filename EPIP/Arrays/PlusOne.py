#add one to an array of integers
#  cant bruteforce because of integer overflow.
# operate directly on the arr

def plusOne(arr):
    arr[-1] += 1
    if arr[-1] < 10:
        return arr
    for i in reversed(range(1, len(arr))):
        if arr[i] >= 10:
            arr[i] = 0
            arr[i - 1] += 1          
    if arr[0] == 10:
        arr[0] = 1
        arr.append(0)

    return arr

print(plusOne([2,3,9]))
        
            
        
