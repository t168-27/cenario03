from copy import deepcopy
from . import *

from .matrix import Matrix, _get_element_index
from .vector import Vector

"""
linearalgebra
=====

Provides
  1. TO DO

TO DO
----------------------------

"""
def _matrix_to_lines(matrix: Matrix) -> [list]:
    return [matrix.elements[_get_element_index(l, 1, matrix.cols): _get_element_index(l, matrix.cols, matrix.cols) + 1] for l in range(1, matrix.rows+1)]

class LinearAlgebra:
    """
    TO DO


    Returns
    -------
    Vector : vector.Vector
        TO DO

    Examples
    --------
    >>> from cenario import LinearAlgebra
    TO DO

    """
    def _replace_rows(matrix_lines: [list], row1_index: int, row2_index: int) -> [list]:
        """Operacao elementar de troca de linhas."""
        row1 = matrix_lines[row1_index]
        row2 = matrix_lines[row2_index]
        
        matrix_lines[row1_index] = row2
        matrix_lines[row2_index] = row1

        return matrix_lines

    def _multiply_row(matrix_lines: [list], row_index: int, scalar) -> [list]:
        row = matrix_lines[row_index]

        new_row = list(map(lambda element: element * scalar, row))

        matrix_lines[row_index] = new_row

        return matrix_lines

    def _add_rows(matrix_lines: [list], row1_index: int, row2_index: int) -> [list]:
        row1 = matrix_lines[row1_index]
        row2 = matrix_lines[row2_index]

        new_row = [x + y for x, y in zip(row1, row2)]

        matrix_lines[row1_index] = new_row

        return matrix_lines

    def transpose(a):
        new_a = deepcopy(a)

        if isinstance(a, Matrix):
            new_a.rows = a.cols
            new_a.cols = a.rows
            
            for l in range(1, a.rows + 1):
                for c in range(1, a.cols + 1):
                    new_a.set(c,l, a.get(l,c))
            
            return new_a
        
        if isinstance(a, Vector):
            new_a.rows = a.cols
            new_a.cols = a.rows
            
            return new_a

    def sum(a, b):
        if isinstance(a, Matrix) and isinstance(b, Matrix):
            # teste de matriz de mesma ordem
            if a.rows != b.rows or a.cols != b.cols:
                raise Exception(f'Adição de matrizes espera matrizes de mesma ordem mas recebeu {a.rows}x{a.cols} e {b.rows}x{b.cols}.')
            
            elements = [a.elements[i] + b.elements[i] for i in range(0, len(a.elements))]

            return Matrix(a.rows, a.cols, elements)
        
        if isinstance(a, Vector) and isinstance(b, Vector):
            # teste de vetor de mesma ordem
            if a.rows != b.rows or a.cols != b.cols:
                raise Exception(f'Adição de vetores espera vetores de mesma ordem mas recebeu {a.rows}x{a.cols} e {b.rows}x{b.cols}.')
            
            elements = [a.elements[i] + b.elements[i] for i in range(0, len(a.elements))]
            
            c = Vector(len(elements), elements)
            c.rows = a.rows
            c.cols = a.cols

            return c
        
        raise TypeError(f'sum espera argumentos de mesmo tipo mas recebeu {type(a)} e {type(b)}')


    def gauss(a):
        m = _matrix_to_lines(a)
        pivot_row = 0
        pivot_col = 0

        def normalize_col(a: Matrix, col):
            """ Transforma o elemento do pivo em 1 se possivel
            """
            new_a = deepcopy(a)
            has_not_zero_row = False

            if m[pivot_row][0] == 1:
                pivot_row += 1
                return new_m
        
            for current_row in m[pivot_row:]:
                if m[current_row][pivot_col] != 0:
                    has_not_zero_row = True
                    break
            
            if has_not_zero_row == False:
                return new_m

            # for current_row in m[pivot_row:]:
            #     if m[current_row][pivot_col] == 1:


        # for row in m:

        # 1 - Testar se 1,1 é igual a 1, se sim ir para passo 6
        # 2 - Testar se 1,1 a 1,n tem algum elemento dif de zero, se não ir para passo 7
        # 3 - Buscar 1 entre 1,1 a 1,n
        # 4 - Buscar outro valor entre 1,1 a 1,n
        # 5 - Tornar valor diferente de 1 em 1
        # 6 - Zerar valores em 2,1 a 2,n
        # 7 - Repete 1 a 6 com póxima coluna e linha