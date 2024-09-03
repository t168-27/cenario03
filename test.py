from cenario import matrix, vector, LinearAlgebra

matriz_A = matrix.Matrix(3,3,[11, 12, 13, 21, 22, 23, 31, 32, 33])
print(matriz_A)

matriz_B = LinearAlgebra.transpose(matriz_A)
print(matriz_B)

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

matriz_vector = matrix.Matrix(3,1, [1,2,3])

print(matriz_vector.get(2,1))