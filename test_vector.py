from cenario.vector import Vector
from cenario.linear_algebra import LinearAlgebra
from copy import deepcopy

linear_algebra = LinearAlgebra()

vetor_teste = Vector(3, [11, 12, 13])

print("Transposta de vetor ", end='')
vetor_esperado = deepcopy(vetor_teste)
vetor_esperado.rows, vetor_esperado.cols = 3, 1
vetor_resultado = linear_algebra.transpose(vetor_teste)

try:
    assert vetor_resultado.elements == vetor_esperado.elements
    assert vetor_resultado.dim == vetor_esperado.dim
    assert vetor_resultado.rows == vetor_esperado.rows
    assert vetor_resultado.cols == vetor_esperado.cols
    print("[OK]")
except:
    print("[Erro]")
    print(f"\nErro: Transposta vetor esperado: \n\n {vetor_resultado} \n\n mas foi recebido: \n\n {vetor_resultado}")


print("Método Vector.get ", end='')
lista_esperada = [11, 12, 13]
lista_resultado = [vetor_teste.get(1), vetor_teste.get(2), vetor_teste.get(3)]

try:
    assert lista_esperada == lista_resultado
    print("[OK]")
except:
    print("[Erro]")
    print(f"\nErro: Lista esperada era \n\n {lista_esperada} \n\n mas foi recebida \n\n {lista_resultado}.")


print("Método Vector.set ", end='')
lista_esperada = [0, 1, 2]

vetor_resultado = deepcopy(vetor_teste)

vetor_resultado.set(1,0)
vetor_resultado.set(2,1)
vetor_resultado.set(3,2)

lista_resultado = [vetor_resultado.get(1), vetor_resultado.get(2), vetor_resultado.get(3)]

try:
    assert lista_esperada == lista_resultado
    print("[OK]")
except:
    print("[Erro]")
    print(f"\nErro: Lista esperada era {lista_esperada} mas foi recebida {lista_resultado}.")


print("Método Vector.set ", end='')
lista_esperada = [0, 1, 2]

vetor_resultado = deepcopy(vetor_teste)

vetor_resultado.set(1,0)
vetor_resultado.set(2,1)
vetor_resultado.set(3,2)

lista_resultado = [vetor_resultado.get(1), vetor_resultado.get(2), vetor_resultado.get(3)]

try:
    assert lista_esperada == lista_resultado
    print("[OK]")
except:
    print("[Erro]")
    print(f"\nErro: Lista esperada era {lista_esperada} mas foi recebida {lista_resultado}.")


vetor_teste_2 = Vector(3, [2,3,4])

print("Método LinearAlgebra.sum (Vector) (Coluna) ", end='')
vetor_esperada = Vector(3, [13,15,17])
tmp_vetor_teste = deepcopy(vetor_teste)
tmp_vetor_teste_2 = deepcopy(vetor_teste_2)
tmp_vetor_teste = linear_algebra.transpose(tmp_vetor_teste)
tmp_vetor_teste_2 = linear_algebra.transpose(tmp_vetor_teste_2)
vetor_esperada.rows = 3
vetor_esperada.cols = 1
vetor_resultado = linear_algebra.sum(tmp_vetor_teste, tmp_vetor_teste_2)

try:
    assert vetor_resultado.elements == vetor_esperada.elements
    assert vetor_resultado.dim == vetor_esperado.dim
    assert vetor_resultado.rows == vetor_esperada.rows
    assert vetor_resultado.cols == vetor_esperada.cols
    print("[OK]")
except:
    print("[Erro]")
    print(f"\nErro: Vetor somado esperado: \n\n {vetor_esperada} \n\n mas foi recebido: \n\n {vetor_resultado}")


print("Método LinearAlgebra.sum (Vector) (Linha) ", end='')
vetor_esperada = Vector(3, [13,15,17])
vetor_resultado = linear_algebra.sum(vetor_teste, vetor_teste_2)

try:
    assert vetor_resultado.elements == vetor_esperada.elements
    assert vetor_resultado.dim == vetor_esperado.dim
    assert vetor_resultado.rows == vetor_esperada.rows
    assert vetor_resultado.cols == vetor_esperada.cols
    print("[OK]")
except:
    print("[Erro]")
    print(f"\nErro: Vetor somado esperado: \n\n {vetor_esperada} \n\n mas foi recebido: \n\n {vetor_resultado}")

print("Método LinearAlgebra.times (Vector) (Coluna) ", end='')
vetor_esperada = Vector(3, [22, 36, 52])
tmp_vetor_teste = deepcopy(vetor_teste)
tmp_vetor_teste_2 = deepcopy(vetor_teste_2)
tmp_vetor_teste = linear_algebra.transpose(tmp_vetor_teste)
tmp_vetor_teste_2 = linear_algebra.transpose(tmp_vetor_teste_2)
vetor_esperada.rows = 3
vetor_esperada.cols = 1
vetor_resultado = linear_algebra.times(tmp_vetor_teste, tmp_vetor_teste_2)

try:
    assert vetor_resultado.elements == vetor_esperada.elements
    assert vetor_resultado.dim == vetor_esperado.dim
    assert vetor_resultado.rows == vetor_esperada.rows
    assert vetor_resultado.cols == vetor_esperada.cols
    print("[OK]")
except:
    print("[Erro]")
    print(f"\nErro: Vetor somado esperado: \n\n {vetor_esperada} \n\n mas foi recebido: \n\n {vetor_resultado}")


print("Método LinearAlgebra.times (Vector) (Linha) ", end='')
vetor_esperada = Vector(3, [22, 36, 52])
vetor_resultado = linear_algebra.times(vetor_teste, vetor_teste_2)

try:
    assert vetor_resultado.elements == vetor_esperada.elements
    assert vetor_resultado.dim == vetor_esperado.dim
    assert vetor_resultado.rows == vetor_esperada.rows
    assert vetor_resultado.cols == vetor_esperada.cols
    print("[OK]")
except:
    print("[Erro]")
    print(f"\nErro: Vetor somado esperado: \n\n {vetor_esperada} \n\n mas foi recebido: \n\n {vetor_resultado}")

vetor_teste_3 = linear_algebra.transpose(Vector(3, [3,1,1]))

print("Método LinearAlgebra.dot (Vector) ", end='')
vetor_esperado = Vector(1, [13])
vetor_resultado = linear_algebra.dot(vetor_teste_2, vetor_teste_3)

try:
    assert vetor_resultado.elements == vetor_esperado.elements
    assert vetor_resultado.dim == vetor_esperado.dim
    assert vetor_resultado.rows == vetor_esperado.rows
    assert vetor_resultado.cols == vetor_esperado.cols
    print("[OK]")
except:
    print("[Erro]")
    print(f"\nErro: Vetor somado esperado: \n\n {vetor_esperada} \n\n mas foi recebido: \n\n {vetor_resultado}")