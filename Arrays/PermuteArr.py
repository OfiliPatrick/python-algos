def permute(arr, perm):
    out = [0] * len(arr)

    i= 0
    for pos in perm:
        out[pos] = arr[i]
        i += 1
    return out



arr = ['a', 'b', 'c', 'd']
perm = [2,0,1,3]
print(permute(arr,perm))