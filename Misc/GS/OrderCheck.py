def orderCheck(height):
    ordered = sorted(height)
    out_of_place = 0

    for i in range(len(height)):
        if height[i] != ordered[i]:
            out_of_place += 1    

    return out_of_place

# print(orderCheck([1, 1, 3, 3, 4, 1]))
# print(orderCheck([1,1,3,4,1]))

