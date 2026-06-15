def search_matrix(mat, N, M, X):
    row = 0
    col = M - 1
    
    while row < N and col >= 0:
        if mat[row][col] == X:
            return 1
        elif mat[row][col] > X:
            col -= 1
        else:
            row += 1
    return 0
