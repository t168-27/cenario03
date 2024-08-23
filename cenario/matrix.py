"""
matrix
=====

Provides
  1. TO DO

TO DO
----------------------------

"""

class Matrix:
    def __init__(self, rows: int, cols: int, elements):
        """
        TO DO

        Parameters
        ----------
        rows : int
            TO DO
        cols : int
            TO DO
        elements : array_like
            TO DO

        Returns
        -------
        Matrix : matrix.Matrix
            TO DO

        Examples
        --------
        >>> from cenario import matrix
        >>> elementos = [11, 12, 13, 21, 22, 23, 31, 32, 33]
        >>> matriz_A = matrix.Matrix(3, 3, elementos)

        >>> matriz_A
        TO DO

        """
        
        if len(elements) != (rows * cols):
            raise Exception(f'Matriz {rows} X {cols} precisa de {(rows * cols)} elementos mas {len(elements)} foram fornecidos.')
        
        self.rows = rows
        self.cols = cols
        self.elements = elements


    def _get_element_index(self, row: int, col: int) -> int:
        return ((row-1) * self.cols) + (col-1)

    
    def get(self, i: int, j: int) -> int:
        return self.elements[self._get_element_index(i, j)]

    
    def set(self, i: int, j: int, value):
        self.elements[self._get_element_index(i, j)] = value