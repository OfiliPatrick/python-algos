import random

def offlineData(arr, k):
    out = []
    import collections
    seen = collections.defaultdict(bool)
    while True:
        rand = random.randint(0, len(arr) - 1)
        if seen[arr[rand]] == False:
            out.append(arr[rand])
            seen[arr[rand]] = True
        if len(out) == k:
            break
    return out

print(offlineData([3,7,5,11],3))