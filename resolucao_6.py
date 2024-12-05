from cenario.matrix import Matrix
from cenario.linear_algebra import LinearAlgebra
from cenario import matrix_to_columns

# define função de iteração do vetor autoridade
def iterate_autority(A_t_A_product, a_previous):

    aux = linear_algebra.dot(A_t_A_product, a_previous)
    
    norm = 1 / ((sum(map(lambda x: x ** 2, aux.elements))) ** (1/2))

    a_k = linear_algebra.times( aux, Matrix( A_t_A_product.rows, 1, [norm for _ in range(A_t_A_product.rows)] ) )

    return a_k

# Definição das constantes
linear_algebra = LinearAlgebra()

A = Matrix(4, 4, [0,1,1,0,0,0,1,0,1,0,0,1,1,0,0,0])

A_t = linear_algebra.transpose(A)

A_t_A_product = linear_algebra.dot(A_t, A)


# Inicio do cálculo
a_0 = Matrix(A.rows, 1, list(map(lambda c: sum(c), matrix_to_columns(A))))

a_1 = iterate_autority(A_t_A_product, a_0)

print("a_1")
print(a_1, end='\n\n')

# Setup para o loop
a_previous = a_1

diff = 1

i = 2

while (diff >= 0.00001 and i < 1000):

    a_k = iterate_autority(A_t_A_product, a_previous)

    print(f"a_{i}")
    print(a_k, end='\n\n')
    
    # pega a maior diferença valor a valor entre a_k e a_previous    
    diff = max(linear_algebra.sum(a_k, Matrix(A_t_A_product.rows, 1, list(map(lambda x: x * -1, a_previous.elements)))).elements)

    print(f"Diferença (a{i} - a{i - 1}): {diff:.5f}", end='\n\n\n')

    a_previous = a_k

    i += 1

if i == 1000:
    print("Os valores de a_k e a_previous não se aproximaram.")

else:
    print("Resultado: ")
    print(a_k)