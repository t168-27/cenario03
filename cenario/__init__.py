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
    def _replace_row(matrix_lines: [list], row1_index, row2_index) -> [list]:
        """Operacao elementar de troca de linhas."""
        row1 = matrix_lines[row1_index]
        row2 = matrix_lines[row2_index]
        
        matrix_lines[row1_index] = row2
        matrix_lines[row2_index] = row1

        return matrix_lines

    def _multiply_row(matrix_lines: [list], row_index, scalar) -> [list]:
        row = matrix_lines[row_index]

        new_row = list(map(lambda element: element * scalar, row))

        matrix_lines[row_index] = new_row

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