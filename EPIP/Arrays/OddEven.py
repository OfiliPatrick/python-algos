#Arrange ele in arr such that even num comes first before odd

#constant space and linear time
def oddEven(arr):
    even_point = 0
    odd_point = len(arr) - 1

    def isEven(num):
        return num %2 ==0
    while even_point < odd_point:
        if isEven(arr[even_point]):
            even_point += 1          
        else:
            arr[even_point], arr[odd_point] = arr[odd_point], arr[even_point]
            odd_point -= 1       
    return arr
    

print(oddEven([2, 1, 3, 7, 2, 0, 2]))


# import bisect
# l = [1, 2, 4, 6, 7, 9]

# print(bisect.bisect_right(l,7))