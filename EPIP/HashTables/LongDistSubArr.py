# not passing second test case

def longDistSubArr(arr):
    first = 0
    second = 1
    lent = 1
    seen = set(arr[0])
    max_lent = - float('inf')

    while first < len(arr) and second < len(arr):
        print(seen)
        if arr[second] not in seen:
            seen.add(arr[second])
            lent += 1
            second += 1
            
        else:
            seen = set(arr[first])
            first += 1
            max_lent= max(max_lent, lent)
            lent = 1
           
        
    return max_lent

print(longDistSubArr(['f', 's', 'f', 'e', 't', 'w', 'e', 'n', 'w', 'e']))
# print(longDistSubArr(['f','f','f','e','t','w','e','n','w','e']))


