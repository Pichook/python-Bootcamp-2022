import numpy as np

def matrix_subtraction(mat1, mat2):
    print("\nMatrix 1:\n\n", str(mat1).replace('[', '').replace(']', ''))
    print("\nMatrix 2:\n\n", str(mat2).replace('[', '').replace(']', ''))
    minus = mat1 - mat2
    print("\nThe result matrix is:\n\n", str(minus).replace('[', '').replace(']', ''),"\n")




mat1 = np.array([[10, 5, 4, 2], [5, 10, 9, 55], [9, 19, 69, 8], [7, 8, 4, 75]])
mat2 = np.array([[12, 65, 34, 2], [1, 5, 8, 45], [7, 21, 63, 8], [0, 78, 4, 65]])

matrix_subtraction(mat1, mat2)
