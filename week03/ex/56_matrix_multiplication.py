import numpy as np

def matrix_multiplication(mat1, mat2):
    res = 0
    for i in range(len(mat1)):
        for j in range(len(mat2)[0]):
            for k in range(len(mat2)):
                mult = res[i][j] + (mat1[k][j] * mat2[k][j])
    print(mult)



mat1 = np.array([[10, 5, 4, 2], [5, 10, 9, 55], [9, 19, 69, 8], [7, 8, 4, 75]])
mat2 = np.array([[12, 65, 34, 2], [1, 5, 8, 45], [7, 21, 63, 8], [0, 78, 4, 65]])
matrix_multiplication(mat1, mat2)

