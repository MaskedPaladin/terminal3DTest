def matrixMul(a, b):
    matrix = [[0,0,0]for i in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                matrix[i][j] = a[i][k]*b[k][j]
    return matrix
def matrixSum(a, b):
    matrix = [[0,0,0]for i in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                matrix[i][j] = a[i][k]+b[k][j]
    return matrix
