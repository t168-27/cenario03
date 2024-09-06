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

def _matrix_to_columns(matrix: Matrix) -> [list]:
    return [[matrix.elements[i] for i in list(range(j - 1, ((matrix.rows - 1) * matrix.cols) + j, matrix.cols))] for j in range(1, matrix.cols + 1)]

class LinearAlgebra:
    """
    TO DO

    Parameters
    ----------
    debug : boolean
        (Opcional) Ativa o print das operações.

    Returns
    -------
    Vector : vector.Vector
        TO DO

    Examples
    --------
    >>> from cenario import LinearAlgebra
    TO DO

    """
    def __init__(self, debug = False):
        self.debug = debug

    def _replace_rows(self, matrix_lines: [list], row1_index: int, row2_index: int) -> [list]:
        """Operacao elementar de troca de linhas."""
        if self.debug: print(f"Trocando linha {row1_index +1 } com linha {row2_index +1}")
        row1 = matrix_lines[row1_index]
        row2 = matrix_lines[row2_index]
        
        matrix_lines[row1_index] = row2
        matrix_lines[row2_index] = row1

        return matrix_lines

    def _multiply_row(self, matrix_lines: [list], row_index: int, scalar) -> [list]:
        if self.debug: print(f"Multiplicando linha {row_index +1 } por {scalar}")
        row = matrix_lines[row_index]

        new_row = list(map(lambda element: element * scalar, row))

        matrix_lines[row_index] = new_row

        return matrix_lines

    def _add_rows(self, matrix_lines: [list], row1_index: int, row2_index: int, scalar = 1) -> [list]:
        row1 = matrix_lines[row1_index]
        row2 = matrix_lines[row2_index]

        new_row = [x + y for x, y in zip(row1, list(map(lambda element: element * scalar, row2)))]

        matrix_lines[row1_index] = new_row

        return matrix_lines

    def transpose(self, a):
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

    def sum(self, a, b):
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


    def gauss(self, a):
        m = _matrix_to_lines(a)
        pivot_row = 0
        pivot_col = 0

        def zero_below_pivot(matrix, pivot_row: int, j: int):
            for i in range(pivot_row + 1, len(matrix)):
                if matrix[i][j] != 0:
                    new_matrix = self._add_rows(matrix, i, pivot_row, matrix[i][j]*-1)
                    if self.debug: print(new_matrix)
            
            return new_matrix

        ii = -1
        while pivot_row < a.rows -1:
            ii += 1
            if self.debug: print({'pivot_col': pivot_col, 'pivot_row': pivot_row})
            if self.debug: print("iniciando linha "+ str(ii))

            pivot_col_elements = [row[pivot_col] for row in m[pivot_row:]]            
            if self.debug: print(pivot_col_elements)
            
            # checa se o pivo já tem valor 1
            if 1 in pivot_col_elements:
                if pivot_col_elements[0] != 1:
                    m = self._replace_rows(m, pivot_row, pivot_col_elements.index(1) + pivot_row)
                    if self.debug: print(m)
                m = zero_below_pivot(m, pivot_row, pivot_col)
                if self.debug: print(m)
            
            elif any(pivot_col_elements):
                for e in pivot_col_elements:
                    if e != 0:
                        i = pivot_col_elements.index(e) + pivot_row
                        m  = self._multiply_row(m, i, (1 / e))
                        if self.debug: print(m)
                        m = self._replace_rows(m, pivot_row, i)
                        if self.debug: print(m)
                        m = zero_below_pivot(m, pivot_row, pivot_col)
                        break
            
            else:
                pivot_col += 1
                continue
                
            pivot_row += 1
            pivot_col += 1

        if m[pivot_row][pivot_col] not in [0,1]:
            m = self._multiply_row(m, pivot_row, (1 / m[pivot_row][pivot_col]))
        
        return Matrix(a.rows, a.cols, [round(e, 4) for l in m for e in l])

    def determinant(self, m: Matrix) -> float:
        if m.rows != m.cols:
            raise Exception(f'_determinant(m) espera uma matriz quadrada mas recebeu uma matriz {m.rows}x{m.cols}.')

        rows = _matrix_to_lines(m)
        cols = _matrix_to_columns(m)

        have_null_row = not all([any(row) for row in rows])
        have_null_col = not all([any(col) for col in cols])
        
        have_equal_rows = len(rows) != len(list(set([tuple(row) for row in rows])))
        have_equal_cols = len(cols) != len(list(set(tuple(col) for col in cols)))
        
        if have_null_row or have_null_col or have_equal_rows or have_equal_cols:
            return 0

        if m.rows == 2:
            return (m.get(1,1) * m.get(2,2)) - (m.get(1,2) * m.get(2,1))
        else:
            row_to_expand = 1
            det = 0.0

            l = list(range(1, m.rows + 1))
            c = list(range(1, m.cols + 1))

            l.remove(row_to_expand)

            for k, e in enumerate(rows[row_to_expand - 1]):
                c_submatrix = [j for j in c if j != (k + 1)]
                submatrix = Matrix(m.rows - 1, m.cols - 1, [m.get(i,j) for i in l for j in c_submatrix])
                cofactor = ((-1) ** (row_to_expand + k + 1)) * determinant(submatrix)
            

    def solve(self, a) -> Matrix:
        ...