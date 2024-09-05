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
    def _replace_rows(self, matrix_lines: [list], row1_index: int, row2_index: int) -> [list]:
        """Operacao elementar de troca de linhas."""
        print(f"Trocando linha {row1_index +1 } com linha {row2_index +1}")
        row1 = matrix_lines[row1_index]
        row2 = matrix_lines[row2_index]
        
        matrix_lines[row1_index] = row2
        matrix_lines[row2_index] = row1

        return matrix_lines

    def _multiply_row(self, matrix_lines: [list], row_index: int, scalar) -> [list]:
        print(f"Multiplicando linha {row_index +1 } por {scalar}")
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
            for i in range(pivot_row + 1, len(matrix)): # enumerate(m[pivot_row:]):
                if matrix[i][j] != 0:
                    new_matrix = self._add_rows(matrix, i, pivot_row, matrix[i][j]*-1)
                    print(new_matrix)
            
            return new_matrix

        for ii in range(0, a.rows - 1):
            print("iniciand linha "+ str(ii))
            no_process = False
            # checa se o pivo já tem valor 1
            if m[pivot_row][pivot_col] == 1:
                no_process = True

            if not no_process:
                pivot_col_elements = [row[pivot_col] for row in m[pivot_row:]]
                print(pivot_col_elements)

            if 1 in pivot_col_elements:
                m = self._replace_rows(m, pivot_row, pivot_col_elements.index(1) + pivot_row)
                print(m)
                m = zero_below_pivot(m, pivot_row, pivot_col)
                print(m)
            
            elif any(pivot_col_elements):
                for e in pivot_col_elements:
                    if e != 0:
                        i = pivot_col_elements.index(e) + pivot_row
                        m  = self._multiply_row(m, i, (1 / e))
                        print(m)
                        m = self._replace_rows(m, pivot_row, i)
                        print(m)
                        m = zero_below_pivot(m, pivot_row, pivot_col)
                        break
                
            pivot_row += 1
            pivot_col += 1

        m = self._multiply_row(m, pivot_row, (1 / m[pivot_row][pivot_col]))
        
        return Matrix(a.rows, a.cols, [e for l in m for e in l])

            #     for i in range(pivot_row, len(m)):
            #         if m[i][pivot_col] == 1:
            #             has_unit_pivot = True
            #             unit_pivot = i
            #             continue
                    
            #         elif 
            
            # if not no_process and not has_unit_pivot:
            #     for i in range(pivot_row, len(m)):
            #         if m[i][pivot_col] != 0:
            #             has_not_zero_pivot = True
            #             not_zero_pivot


            # # checa se existe valor 1 na coluna
            # for i in range(pivot_row, len(m)):
            # # for current_row_index, current_row in enumerate(m[pivot_row:]):
            #     if m[i][pivot_col] == 1:
            #         m = self._replace_rows(m, pivot_row, i)
            #         print(m)
            #         m = zero_below_pivot(m, pivot_row, pivot_col)
            #         print(m)

            #         finished = True
            #         continue
                                
            # if finished: 
            #     pivot_row += 1
            #     pivot_col += 1
            #     continue

            # # checa se na coluna atual existe valor diferente de zero
            # for i in range(pivot_row, len(m)):
            #     if m[i][pivot_col] != 0:
            #         m  = self._multiply_row(m, i, (1 / m[i][pivot_col]))
            #         print(m)
            #         m = self._replace_rows(m, pivot_row, i)
            #         print(m)
            #         # transformar pivot em 1
            #         m = zero_below_pivot(m, pivot_row, pivot_col)

                
                
                
            # if m[current_row_index + pivot_row][pivot_col] != 0:
                    # m = self._replace_rows(m, pivot_row, current_row_index + pivot_row)
                    # print(m)
                    # for current_row_index, current_row in enumerate(m[pivot_row:]):
                    #     if m[current_row_index + pivot_row][pivot_col] == 1:
                    #         m = self._replace_rows(m, pivot_row, current_row_index + pivot_row)
                    #         print(m)
                    #         for row_to_zero_index, row_to_zero in enumerate(m[pivot_row:]):
                    #             if row_to_zero_index <= pivot_row: continue
                    #             if m[row_to_zero_index][pivot_col] != 0:
                    #                 m = self._add_rows(m, row_to_zero_index, pivot_row, row_to_zero[0]*-1)
                    #                 print(m)                    
                    #         continue


            
            # termina operacao se a coluna só tem valores igual a zero
            # if no_process:
            #     pivot_row += 1
            #     pivot_col += 1
            
        # return pivot_col_elements
        # print(type(m))

        # for row in m:

        # 1 - Testar se 1,1 é igual a 1, se sim ir para passo 6
        # 2 - Testar se 1,1 a 1,n tem algum elemento dif de zero, se não ir para passo 7
        # 3 - Buscar 1 entre 1,1 a 1,n
        # 4 - Buscar outro valor entre 1,1 a 1,n
        # 5 - Tornar valor diferente de 1 em 1
        # 6 - Zerar valores em 2,1 a 2,n
        # 7 - Repete 1 a 6 com póxima coluna e linha