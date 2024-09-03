from copy import deepcopy
from . import *

from .matrix import Matrix, _get_element_index

"""
linearalgebra
=====

Provides
  1. TO DO

TO DO
----------------------------

"""

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
    def transpose(a):
        new_a = deepcopy(a)
        for l in range(1, a.rows + 1):
            for c in range(1, a.cols + 1):
                if l != c:
                    new_a.set(c,l, a.get(l,c))
        
        return new_a