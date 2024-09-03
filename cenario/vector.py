"""
vector
=====

Provides
  1. TO DO

TO DO
----------------------------

"""

class Vector:
    """
    TO DO

    Parameters
    ----------
    dim : int
        TO DO
    elements : array_like
        TO DO

    Returns
    -------
    Vector : vector.Vector
        TO DO

    Examples
    --------
    >>> from cenario import vector
    >>> elementos = [11, 12, 13]
    >>> vector_a = vector.Vector(3, 3, elementos)

    >>> vector_a
    TO DO

    """
    def __init__(self, dim: int, elements: [int]):
            self.dim = dim
            self.elements = elements
    
    def __repr__(self) -> str:
            return repr(self.elements)

    def get(self, i: int) -> int:
        return self.elements[i-1]

    def set(self, i: int, value: int) -> int:
        self.elements[i-1] = value