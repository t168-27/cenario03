from . import *

from .matrix import Matrix, _get_element_index

"""
cenario
=====

Provides
  1. TO DO

TO DO
----------------------------

"""
def _matrix_to_lines(matrix: Matrix) -> [list]:
    return [matrix.elements[_get_element_index(i, 1, matrix.cols): _get_element_index(i, matrix.cols, matrix.cols) + 1] for i in range(1, matrix.rows+1)]

def _matrix_to_columns(matrix: Matrix) -> [list]:
    return [[matrix.elements[i] for i in list(range(j - 1, ((matrix.rows - 1) * matrix.cols) + j, matrix.cols))] for j in range(1, matrix.cols + 1)]