def rotImg(arr):
    # first transpose because switching cols is easier than switching a row and a col
    #for each row index start at a col index equal to it so you wont visit a previous index and change its value
    def transpose(arr):
        for row in range(len(arr)):
            for col in range(row,len(arr)):
                arr[row][col], arr[col][row] = arr[col][row], arr[row][col] 

    # use two pointer to switch col symmetrically
    def switch(arr):
        first = 0
        last = len(arr) - 1
        while first < last:
            for row_access in range(0, len(arr)):
                arr[row_access][first], arr[row_access][last] = arr[row_access][last], arr[row_access][first]
            first += 1
            last-=1
    transpose(arr)
    switch(arr)
    return arr

arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

arr2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(rotImg(arr))