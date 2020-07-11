def delDupSort(arr):
    first = 0
    second = 1

    while first < len(arr) and second < len(arr):
        if arr[first] != arr[second]:
            first += 1
            arr[first] = arr[second]
            second += 1
            
        else:
            second += 1

    for i in range(first+1):
        print(arr[i])


print(delDupSort([1,2,3,4]))
