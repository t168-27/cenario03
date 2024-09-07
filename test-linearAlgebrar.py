from cenario.linearAlgebrar import LinearAlgebra as La
from cenario.matrix import Matrix as Mx
from cenario.vector import Vector as Vc

"""
Exemplos de transposta: 
Exp01: 
A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

Resultado:
A^T = [
    [1, 4],
    [2, 5],
    [3, 6]
]

B^T = [
    [7, 9, 11],
    [8, 10, 12]
]

A + B = None

A + B^T =  [
    [8, 11, 14]
    [12, 15, 18]
]

A * B = None

A * B^T = [
    [7, 18, 33],   
    [8, 50, 72]
]

Exp02:
VecA = [1,2,3]
VecB = [4,5,6]

Resultado:
VecA^T = [
    [1],
    [2],
    [3]
]

VecB^T = [
    [4],
    [5],
    [6]
]

VecA + VecB = [5, 7, 9]

VecA * VecB = [4, 10, 18]

"""
# "Exemplo 01"
# "Matrix A e B"
# TestA = Mx(2,3,[1, 2, 3, 4, 5, 6])
# print(f'Matrix A: \n {TestA}')

# TestB = Mx(3,2,[7, 8, 9, 10, 11, 12])
# print(f'Matrix B: \n {TestB}')

# "Transposta de A"
# # TestA = La.transpose(TestA)
# # print(f'Matrix A^T: {TestA}')

# "Transposta de B"
# TestB = La.transpose(TestB)
# print(f'Matrix B^T: \n {TestB}')


# "Soma de A com B"
# SumAB = La.sum(TestA, TestB)
# print(f'Matrix A + B: \n {SumAB}')


# "Times de A com B"
# TimesAB = La.times(TestA, TestB)
# print(f'Matrix A * B: \n {TimesAB}')

# "Dot de A com B"
# DotAB = La.dot(TestA, TestB)
# print(f'Matrix A * B: \n {DotAB}')


# "Exemplo 02:"

# "Vector A e B"
# VecA = Vc(3,[1,2,3])
# print(f'Vector A: \n{VecA}')

# VecB = Vc(3,[4,5,6])
# print(f'Vector B: \n{VecB}')

# "Transposta de VecA"
# VecAT = La.transpose(VecA)
# print(f'Vec A^T: \n{VecAT}')

# "Transposta de VecB"
# VecBT = La.transpose(VecB)
# print(f'Vec B^T: \n{VecBT}')

# "Soma de VecA com VecB"
# SumVecAB = La.sum(VecA, VecB)
# print(f'Vec A + B: \n{SumVecAB}')

# "Times de VecA com VecB"
# TimesVecAB = La.times(VecA, VecB)
# print(f'Vec A * B: \n{TimesVecAB}')

# "Dot de VecA com VecB"
# DotVecAB = La.dot(VecA, VecB)
# print(f'Vec A * B: \n{DotVecAB}')

import numpy as np

a = [[1, 2, 3], [4, 5, 6]]
b = [[7, 8], [9, 10], [11, 12]]

print(np.dot(a,b))
