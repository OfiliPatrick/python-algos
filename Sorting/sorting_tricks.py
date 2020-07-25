sorted_index_score = sorted(index_score, key=lambda num: num[1], reverse=True)

new_tuple = sorted(d.items(), key = operator.itemgetter(1))

#to inverse a matrix sort of
for listt in arr:
    for index,j in enumerate(listt):
        d[index].append(j)


for j in range(len(mat[0])):
    temp=[]
    for i in range(len(mat)):
        temp.append(matr[i][j])


 neighbors = lambda grid, x, y : [grid[x2][y2] for x2 in range(x-1, x+2)
    for y2 in range(y-1, y+2)
    if (-1 < x <= X and
        -1 < y <= Y and
        (x != x2 or y != y2) and
        (0 <= x2 <= X) and
        (0 <= y2 <= Y) and x2<= len(grid) -1 and y2 <= len(grid[0])-1 and grid[x2][y2] ==1 )]