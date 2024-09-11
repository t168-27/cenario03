from copy import deepcopy
from . import matrix_to_lines, matrix_to_columns, lines_to_matrix, columns_to_matrix
from .matrix import Matrix, get_element_index
from .vector import Vector

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
        """Operacao elementar de troca de linha por ela multiplicado por escalar."""
        if self.debug: print(f"Multiplicando linha {row_index +1 } por {scalar}")
        row = matrix_lines[row_index]

        new_row = list(map(lambda element: element * scalar, row))

        matrix_lines[row_index] = new_row

        return matrix_lines


    def _add_rows(self, matrix_lines: [list], row1_index: int, row2_index: int, scalar = 1) -> [list]:
        """Operacao elementar de troca de linha por ela somada por outra linha."""
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
        
            for p in range(1, a.rows + 1):
                for k in range(1, a.cols + 1):
                    aux = a.get(p,k)
                    new_a.set(k, p, aux)

            return new_a

        if isinstance(a, Vector):
            new_a.rows = a.cols
            new_a.cols = a.rows
            return new_a


    def sum(self, a, b):
        if isinstance(a, Matrix) and isinstance(b, Matrix):
            if a.rows != b.rows or a.cols != b.cols:
                raise ValueError(f'Adição de matrizes espera matrizes de mesma ordem mas recebeu {a.rows}x{a.cols} e {b.rows}x{b.cols}.')
            new_a = deepcopy(a)
            for p in range(1, a.rows + 1):
                for k in range(1, a.cols + 1):
                    aux = a.get(p,k) + b.get(p,k)
                    new_a.set(p, k, aux)
            return new_a
        
        elif isinstance(a, Vector) and isinstance(b, Vector):
            if a.rows != b.rows or a.cols != b.cols:
                raise ValueError(f'Adição de vetores espera vetores de mesma ordem mas recebeu {a.rows}x{a.cols} e {b.rows}x{b.cols}.')
            new_a = deepcopy(a)
            for k in range(1, len(a.elements) + 1):
                aux = a.get(k) + b.get(k)
                new_a.set(k, aux)
            return new_a
        
        else:
            raise TypeError(f"LinearAlgebra.sum requer dois objetos Vector ou Matrix mas recebeu {type(a)} e {type(b)}")


    def times(self, a, b):
        if isinstance(a, Matrix) and isinstance(b, Matrix):
            if a.rows != b.rows or a.cols != b.cols:
                return ValueError(f'Multiplição elemento a elemento de matrizes espera matrizes de mesma ordem mas recebeu {a.rows}x{a.cols} e {b.rows}x{b.cols}.')
            new_a = deepcopy(a)
            for p in range(1, a.rows + 1):
                for k in range(1, a.cols + 1):
                    aux = a.get(p, k) * b.get(p, k)
                    new_a.set(p, k, aux)
            return new_a
        
        if isinstance(a, Vector) and isinstance(b, Vector):
            if a.rows != b.rows or a.cols != b.cols:
                return ValueError(f'Multiplição elemento a elemento de vetores espera vetores de mesma ordem mas recebeu {a.rows}x{a.cols} e {b.rows}x{b.cols}.')
            new_a = deepcopy(a)
            for k in range(1, len(a.elements) + 1):
                aux = a.get(k) * b.get(k)
                new_a.set(k, aux)
            return new_a


    def dot(self, a, b) -> Matrix:
        if a.cols != b.rows:
            raise ValueError(f'LinearAlgebra.dot requer um número de colunas do primeiro objeto igual ao de linhas do segundo mas recebeu {a.cols} e {b.rows}.')

        if isinstance(a, Vector) and isinstance(b, Vector):
            return Matrix(1, 1, [sum([ea * eb for ea, eb in zip(a.elements, b.elements)])])

        elif isinstance(a, Matrix) and isinstance(b, Matrix):
            a_rows = matrix_to_lines(a)
            b_cols = matrix_to_columns(b)

            elements = []

            for row in a_rows:
                a_row = Vector(a.cols, row)
                for col in b_cols:
                    elements.append(self.dot(a_row, self.transpose(Vector(b.rows, col))).get(1,1))

            return Matrix(a.rows, b.cols, elements) 

        else:
            raise TypeError(f"LinearAlgebra.dot requer dois objetos Vector ou Matrix mas recebeu {type(a)} e {type(b)}")


    def gauss(self, a):
        m = matrix_to_lines(a)
        pivot_row = 0
        pivot_col = 0

        def zero_below_pivot(matrix, pivot_row: int, j: int):
            for i in range(pivot_row + 1, len(matrix)):
                if matrix[i][j] != 0:
                    new_matrix = self._add_rows(matrix, i, pivot_row, matrix[i][j]*-1)
                    if self.debug: print(new_matrix)
                else:
                    new_matrix = deepcopy(matrix)
            
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


    def solve(self, a) -> Matrix:
        reduced_a = self.gauss(a)
        
        cols_a = matrix_to_columns(reduced_a)
        coefficient_cols = cols_a[:-1]
        b = cols_a[-1]
        
        coefficient_matrix = columns_to_matrix(coefficient_cols)
        coefficient_rows = matrix_to_lines(coefficient_matrix)

        for row in coefficient_rows:
            if not any(row):
                raise Exception("O sistema não tem solução definida ou tem infinitas soluções.")
        
        x_list = [0 for _ in b]
        
        x_list[-1] = b[-1]

        x = self.transpose(Vector(len(b), x_list))

        i = len(b) - 2
        for row in list(reversed(coefficient_rows[:-1])):
            x_value = b[i] - self.dot(Vector(len(row), row), x).get(1,1)
            x.set(i + 1, x_value)
            i -= 1

        return x