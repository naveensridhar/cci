def set_matrix_zero(input):
    row = []
    col = []
    for i in range(0, len(input)):
        for j in range(0, len(input[0])):
            if input[i][j] == 0:
                row.append(i)
                col.append(j)
    print input
    for i in range(0, len(input)):
        for j in range(0, len(input[0])):
            if ((i in row) or (j in col)):
                input[i][j] = 0
    return input

inp = [[10, 0, 5], [6, 5, 1], [0, 1, 5]]
print set_matrix_zero(inp)
