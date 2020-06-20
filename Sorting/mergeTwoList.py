def mergeTwoList(arr1, arr2):

    out = []
    first = 0
    second = 0

    while first < len(arr1) and second < len(arr2):
        if arr1[first] <= arr2[second]:
            out.append(arr1[first])
            first += 1
        else:
            out.append(arr2[second])
            second += 1

    for i in range(first, len(arr1)):
        out.append(arr1[first])

    for i in range(second, len(arr2)):
        out.append(arr2[second])
            
    return out

a = [2, 8, 15, 18]
b =[5,9,12,15,17,20]
print(mergeTwoList(a,b))

        
