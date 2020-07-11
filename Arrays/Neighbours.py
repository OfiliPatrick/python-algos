arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

def getNei(arr, row, col):
    out = []
    def inBound(row, col):
        if 0<= row< len(arr) and 0<=col<len(arr[0]):
            return True
    neis = [(row, col - 1),(row - 1, col-1),(row - 1, col),(row - 1, col + 1), (row, col + 1),(row + 1, col + 1), (row + 1,col), (row+1,col-1)]
    for row,col in neis:
        if inBound(row,col):
            out.append(arr[row][col])

    return out
print(getNei(arr,2,2))