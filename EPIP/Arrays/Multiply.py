# simulate the multiplication of two nums in array form
def multiply(arr1, arr2):
    \
    if arr1[0] > 0 and arr2[0] > 0:
        prefix = 1
    else:
        prefix = -1

    arr1[0] ,arr2[0] = abs(arr1[0]) , abs(arr2[0])
    result = [0] * (len(arr1)+ len(arr2))
    for j in reversed(range(len(arr2))):
        for i in reversed(range(len(arr1))):
            result[j + i + 1] += arr1[j] * arr2[i] 
            result[j + i] += result[j + i + 1] // 10
            result[j + i + 1] %= 10
           
    for num in result:
        if num == 0:
            result.pop(0)
        else:
            break
    
    first = result[0]
    return [(prefix * first)] + result[1:]
            

arr1 = [-2, 4]
arr2 = [3, 5]

print(multiply(arr1,arr2))