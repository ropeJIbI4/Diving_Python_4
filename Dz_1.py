#Напишите функцию для транспонирования матрицы

matrix = [[3, 2, 7, 9],
          [6, 12, 1, 5]]

matrix_1 = [[1, 2, 3, 4],
          [1, 2, 3, 4]]

def trans_matrix(matrix):
    trans_matrix = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
    print(trans_matrix)

print(matrix_1)
print(trans_matrix(matrix_1))