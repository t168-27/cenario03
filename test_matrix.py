from cenario.matrix import Matrix
from cenario.linear_algebra import LinearAlgebra
from copy import deepcopy

linear_algebra = LinearAlgebra()

matriz_teste = Matrix(3,3,[11, 12, 13, 21, 22, 23, 31, 32, 33])

print("Transposta matriz quadrada ", end='')
matriz_esperada = Matrix(3,3,[11, 21, 31, 12, 22, 32, 13, 23, 33])
matriz_resultado = linear_algebra.transpose(matriz_teste)

try:
    assert matriz_resultado.elements == matriz_esperada.elements
    assert matriz_resultado.rows == matriz_esperada.rows
    assert matriz_resultado.cols == matriz_esperada.cols
    print("[OK]")
except:
    print("[Erro]")
    print(f"\nErro: Transposta matriz quadrada esperada: \n\n {matriz_esperada} \n\n mas foi recebida: \n\n {matriz_resultado}\n\n")


print("Método Matrix.get ", end='')
lista_esperada = [11, 12, 13, 21, 22, 23, 31, 32, 33]
lista_resultado = [
    matriz_teste.get(1,1), matriz_teste.get(1,2), matriz_teste.get(1,3),
    matriz_teste.get(2,1), matriz_teste.get(2,2), matriz_teste.get(2,3),
    matriz_teste.get(3,1), matriz_teste.get(3,2), matriz_teste.get(3,3)
    ]

try:
    assert lista_esperada == lista_resultado
    print("[OK]")
except:
    print("[Erro]")
    print(f"\nErro: Lista esperada era \n\n {lista_esperada} \n\n mas foi recebida \n\n {lista_resultado}.\n\n")


print("Método Matrix.set ", end='')
lista_esperada = [0, 1, 2, 10, 11, 12, 20, 21, 22]

matriz_resultado = deepcopy(matriz_teste)

matriz_resultado.set(1,1,0)
matriz_resultado.set(1,2,1)
matriz_resultado.set(1,3,2)
matriz_resultado.set(2,1,10)
matriz_resultado.set(2,2,11)
matriz_resultado.set(2,3,12)
matriz_resultado.set(3,1,20)
matriz_resultado.set(3,2,21)
matriz_resultado.set(3,3,22)

lista_resultado = [
    matriz_resultado.get(1,1), matriz_resultado.get(1,2), matriz_resultado.get(1,3),
    matriz_resultado.get(2,1), matriz_resultado.get(2,2), matriz_resultado.get(2,3),
    matriz_resultado.get(3,1), matriz_resultado.get(3,2), matriz_resultado.get(3,3)
    ]

try:
    assert lista_esperada == lista_resultado
    print("[OK]")
except:
    print("[Erro]")
    print(f"\nErro: Lista esperada era {lista_esperada} mas foi recebida {lista_resultado}.\n\n")


matriz_teste_2 = Matrix(3, 2, [1,2,3,4,5,6])

print("Transposta matriz não-quadrada ", end='')
matriz_esperada = Matrix(2, 3, [1,3,5,2,4,6])
matriz_resultado = linear_algebra.transpose(matriz_teste_2)

try:
    assert matriz_resultado.elements == matriz_esperada.elements
    assert matriz_resultado.rows == matriz_esperada.rows
    assert matriz_resultado.cols == matriz_esperada.cols
    print("[OK]")
except:
    print("[Erro]")
    print(f"\nErro: Transposta matriz quadrada esperada: \n\n {matriz_esperada} \n\n mas foi recebida: \n\n {matriz_resultado}\n\n")


matriz_teste_3 = Matrix(3, 2, [2,3,4,5,6,7])

print("Método LinearAlgebra.sum (Matrix)", end='')
matriz_esperada = Matrix(3, 2, [3,5,7,9,11,13])
matriz_resultado = linear_algebra.sum(matriz_teste_2, matriz_teste_3)

try:
    assert matriz_resultado.elements == matriz_esperada.elements
    assert matriz_resultado.rows == matriz_esperada.rows
    assert matriz_resultado.cols == matriz_esperada.cols
    print("[OK]")
except:
    print("[Erro]")
    print(f"\nErro: Matriz somada esperada: \n\n {matriz_esperada} \n\n mas foi recebida: \n\n {matriz_resultado}\n\n")


print("Método LinearAlgebra.times (Matrix) ", end='')
matriz_esperada = Matrix(3, 2, [2,6,12,20,30,42])
matriz_resultado = linear_algebra.times(matriz_teste_2, matriz_teste_3)

try:
    assert matriz_resultado.elements == matriz_esperada.elements
    assert matriz_resultado.rows == matriz_esperada.rows
    assert matriz_resultado.cols == matriz_esperada.cols
    print("[OK]")
except:
    print("[Erro]")
    print(f"\nErro: Vetor somado esperado: \n\n {matriz_esperada} \n\n mas foi recebido: \n\n {matriz_resultado}")


matriz_teste_4 = Matrix(3,4,[0, -2, 3, 1, 3, 6, -3, -2, 1, 6, 3, 5])

print("Método LinearAlgebra.gauss ", end='')
matriz_esperada = Matrix(3, 4, [1, 6, 3, 5, 0, 1, 1, 1.4167, 0, 0, 1, 0.7667])
matriz_resultado = linear_algebra.gauss(matriz_teste_4)

try:
    assert matriz_resultado.elements == matriz_esperada.elements
    assert matriz_resultado.rows == matriz_esperada.rows
    assert matriz_resultado.cols == matriz_esperada.cols
    print("[OK]")
except:
    print("[Erro]")
    print(f"\nErro: Matriz escalonada esperada: \n\n {matriz_esperada} \n\n mas foi recebida: \n\n {matriz_resultado}\n\n")


matriz_teste_5 = Matrix(4, 5, [1,2,1,1,1,1,2,2,3,3,1,2,6,12,13,2,4,2,4,6])

print("Método LinearAlgebra.gauss (Matriz infinitas soluções) ", end='')
matriz_esperada = Matrix(4, 5, [1, 2, 1, 1, 1, 0, 0, 1, 2, 2, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0])
matriz_resultado = linear_algebra.gauss(matriz_teste_5)

try:
    assert matriz_resultado.elements == matriz_esperada.elements
    assert matriz_resultado.rows == matriz_esperada.rows
    assert matriz_resultado.cols == matriz_esperada.cols
    print("[OK]")
except:
    print("[Erro]")
    print(f"\nErro: Matriz escalonada esperada: \n\n {matriz_esperada} \n\n mas foi recebida: \n\n {matriz_resultado}\n\n")


matriz_teste_6 = Matrix(2, 3, [1, 1, 4, 2, 1, 4])
matriz_teste_7 = Matrix(3, 2, [1, 5, 2, 2, 1, 0])

print("Método LinearAlgebra.dot (Matrix) ", end='')
matriz_esperada = Matrix(2, 2, [7, 7, 8, 12])
matriz_resultado = linear_algebra.dot(matriz_teste_6, matriz_teste_7)

try:
    assert matriz_resultado.elements == matriz_esperada.elements
    assert matriz_resultado.rows == matriz_esperada.rows
    assert matriz_resultado.cols == matriz_esperada.cols
    print("[OK]")
except:
    print("[Erro]")
    print(f"\nErro: Vetor somado esperado: \n\n {matriz_esperada} \n\n mas foi recebido: \n\n {matriz_resultado}")


matriz_teste_8 = Matrix(3, 4, [2, 4, 8, 1, 2, 3, 0, 4, 0, 1, 2, 6])

print("Método LinearAlgebra.solve ", end='')
matriz_esperada = Matrix(3, 1, [-11.5, 9, -1.5])
matriz_resultado = linear_algebra.solve(matriz_teste_8)

try:
    assert matriz_resultado.elements == matriz_esperada.elements
    assert matriz_resultado.rows == matriz_esperada.rows
    assert matriz_resultado.cols == matriz_esperada.cols
    print("[OK]")
except:
    print("[Erro]")
    print(f"\nErro: Matriz coluna X esperada: \n\n {matriz_esperada} \n\n mas foi recebida: \n\n {matriz_resultado}")