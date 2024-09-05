from cenario import matrix, vector, LinearAlgebra, _matrix_to_lines

# print("\nTeste de transposta de matriz quadrada:")
# matriz_A = matrix.Matrix(3,3,[11, 12, 13, 21, 22, 23, 31, 32, 33])
# print(matriz_A)
# matriz_B = LinearAlgebra().transpose(matriz_A)
# print(matriz_B)

# print(matriz_A.get(1,1))
# print(matriz_A.get(1,2))
# print(matriz_A.get(1,3))
# print(matriz_A.get(2,1))
# print(matriz_A.get(2,2))
# print(matriz_A.get(2,3))
# print(matriz_A.get(3,1))
# print(matriz_A.get(3,2))
# print(matriz_A.get(3,3))

# matriz_A.set(1,1,0)
# matriz_A.set(1,2,1)
# matriz_A.set(1,3,2)
# matriz_A.set(2,1,10)
# matriz_A.set(2,2,11)
# matriz_A.set(2,3,12)
# matriz_A.set(3,1,20)
# matriz_A.set(3,2,21)
# matriz_A.set(3,3,22)

# print(matriz_A)


# vector_a = vector.Vector(3, [11, 21, 31])

# print('')
# print(vector_a)

# print(vector_a.get(1))
# print(vector_a.get(2))
# print(vector_a.get(3))

# vector_a.set(1, 0)
# vector_a.set(2, 1)
# vector_a.set(3, 2)

# print(vector_a.get(1))
# print(vector_a.get(2))
# print(vector_a.get(3))

# print("\nTeste de transposta de matriz não quadrada:")
# matriz_C = matrix.Matrix(3, 2, [1,2,3,4,5,6])
# print(matriz_C)

# matriz_D = LinearAlgebra().transpose(matriz_C)
# print(matriz_D)


# print("\nTeste de transposta de vetor:")
# vetor_A = vector.Vector(3, [1,2,3])
# print(vetor_A)

# vetor_B = LinearAlgebra().transpose(vetor_A)
# print(vetor_B)

# print('\nTeste de soma de matrizes: ')
# matriz_A = matrix.Matrix(3, 2, [1,2,3,4,5,6])
# matriz_B = matrix.Matrix(3, 2, [2,3,4,5,6,7])

# print(LinearAlgebra().sum(matriz_A, matriz_B))

# print('\nTeste de soma de vetores linha: ')
# vetor_A = vector.Vector(3, [1,2,3])
# vetor_B = vector.Vector(3, [2,3,4])

# print(LinearAlgebra().sum(vetor_A, vetor_B))

# print('\nTeste de soma de vetores coluna: ')
# vetor_A = vector.Vector(3, [1,2,3])
# vetor_B = vector.Vector(3, [2,3,4])

# vetor_A = LinearAlgebra().transpose(vetor_A)
# vetor_B = LinearAlgebra().transpose(vetor_B)

# print(LinearAlgebra().sum(vetor_A, vetor_B))


matriz_A = matrix.Matrix(3,4,[0, -2, 3, 1, 3, 6, -3, -2, 1, 6, 3, 5])
# print(LinearAlgebra().gauss(matriz_A))

# matriz_resposta = matrix.Matrix(3,4,[1, 2, -1, -(2/3), 0, 1, -(3/2), -(1/2), 0, 0, 0, 1])

print(_matrix_to_lines(matriz_A))

# print(LinearAlgebra()._replace_rows(_matrix_to_lines(matriz_A), 0, 1))
# print(LinearAlgebra()._multiply_row(_matrix_to_lines(matriz_A), 0, 3))
# print(LinearAlgebra()._add_rows(_matrix_to_lines(matriz_A), 0, 1, -1))

print('\n' + str(LinearAlgebra().gauss(matriz_A)))

