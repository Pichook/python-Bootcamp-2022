import numpy as np

def matrix_multiplication(mat1, mat2):
    row1, column1 = mat1.shape
    row2, column2 = mat2.shape

    if column2 == row1: 
        mult = mat1@mat2
        print(mult)
    else: # else block not working at the moment
        print("Error. Row of matrix 1 is not equal to column of matrix 2.")




# mat1 = np.array([[3, 7, 5], [2, 6, 7], [4, 3, 2]])
# mat2 = np.array([[6, 5, 4], [3, 2, 1], [1, 2, 3]])
# matrix_multiplication(mat1, mat2)

mat1 = np.array([[3, 7, 5], [2, 6, 7], [4, 3, 2]])
mat2 = np.array([[6, 5, 4], [3, 2, 1]])
matrix_multiplication(mat1, mat2)

