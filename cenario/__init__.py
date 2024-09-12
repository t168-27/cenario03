from . import *

from .matrix import Matrix, get_element_index

"""
cenario
=====

Provides
  1. Funções auxiliares que serão utilizadas pelos módulos do pacote.
"""


def matrix_to_lines(matrix: Matrix) -> [list]:
    """
    Converte uma matriz para uma lista de linhas.

    Parameters
    ----------
    matrix (Matrix): Um objeto Matrix que será convertido.

    Returns
    -------
    list: Uma lista contendo as linhas da matriz.
    """
    return [matrix.elements[get_element_index(i, 1, matrix.cols): get_element_index(i, matrix.cols, matrix.cols) + 1] for i in range(1, matrix.rows+1)]


def matrix_to_columns(matrix: Matrix) -> [list]:
    """
    Converte uma matriz para uma lista de colunas.

    Parameters
    ----------
    matrix (Matrix): Um objeto Matrix que será convertido.

    Returns
    -------
    list: Uma lista contendo as colunas da matriz.
    """
    return [[matrix.elements[i] for i in list(range(j - 1, ((matrix.rows - 1) * matrix.cols) + j, matrix.cols))] for j in range(1, matrix.cols + 1)]


def lines_to_matrix(lines: [list]) -> Matrix:
    """
    Converte uma lista de linhas em uma matriz.

    Parameters
    ----------
    lines (list): Uma lista de linhas.

    Returns
    -------
    Matrix: A matriz resultante da conversão das linhas.
    """
    return Matrix(len(lines), len(lines[0]), [e for line in lines for e in line])


def columns_to_matrix(columns: [list]) -> Matrix:
    """
    Converte uma lista de colunas em uma matriz.

    Parameters
    ----------
    lines (list): Uma lista de colunas.

    Returns
    -------
    Matrix: A matriz resultante da conversão das colunas.
    """
    return Matrix(len(columns[0]), len(columns), [columns[i][j] for j in range(0, len(columns[0])) for i in range(0, len(columns))])