import numpy as np



def matrix_addition(mat1, mat2):
    sum = mat1 +mat2
    print(f"Matrix 1 =\n {mat1}")
    print(f"Matrix 2 =\n {mat2}")
    print("The result matrix is:\n", sum)

mat1 = np.array([[10, 5, 4, 2], [5, 0, 9, 5], [9, 19, 60, 8], [7, 8, 4, 5]])
mat2 = np.array([[12, 65, 34, 42], [10, 5, 89, 45], [11, 21, 63, 78], [87, 78, 54, 65]])
matrix_addition(mat1, mat2)



