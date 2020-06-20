# go to previous row, get the sum of the element in the previous col and current col

def pascalsTriangle(n):
    result = [[1] * i for i in range(1, n + 1)]
    for row in range(0, n):
        for col in range(1, row):
            prev_row = row - 1
            prev_col = col -1   
            result[row][col] = result[prev_row][prev_col] + result[prev_row][col]

    return result

print(pascalsTriangle(5))