from cenario.matrix import Matrix as mx
from cenario.vector import Vector as vc
from copy import deepcopy

class LinearAlgebra:

    def transpose(a):
        newA = deepcopy(a)
        if isinstance(a, mx):
        
            newA.rows = a.cols
            newA.cols = a.rows
            for p in range(1, a.rows + 1):
                for k in range(1, a.cols + 1):
                    aux = a.get(p,k)
                    newA.set(k,p, aux)

            return newA

        if isinstance(a, vc):
            newA.rows = a.cols
            newA.cols = a.rows
            return newA
        
    def sum(a, b):
        if isinstance(a, mx) and isinstance(b, mx):
            if a.rows != b.rows or a.cols != b.cols:
                return None
            newA = deepcopy(a)
            for p in range(1, a.rows + 1):
                for k in range(1, a.cols + 1):
                    aux = a.get(p,k) + b.get(p,k)
                    newA.set(p,k, aux)
            return newA
        
        if isinstance(a, vc) and isinstance(b, vc):
            if a.cols != b.cols:
                return None
            newA = deepcopy(a)
            for k in range(1, a.cols + 1):
                aux = a.get(k) + b.get(k)
                newA.set(k, aux)
            return newA
    
    def times(a,b):
        if isinstance(a, mx) and isinstance(b, mx):
            if a.rows != b.rows or a.cols != b.cols:
                return None
            newA = deepcopy(a)
            for p in range(1, a.rows + 1):
                for k in range(1, a.cols + 1):
                    aux = a.get(p,k) * b.get(p,k)
                    newA.set(p,k, aux)
            return newA
        
        if isinstance(a, vc) and isinstance(b, vc):
            if a.cols != b.cols:
                return None
            newA = deepcopy(a)
            for k in range(1, a.cols + 1):
                aux = a.get(k) * b.get(k)
                newA.set(k, aux)
            return newA
    
    def dot():
        # - Se A é uma matriz de ordem m×n (ou seja, A tem m linhas e n colunas)
        # - E B é uma matriz de ordem n×p (ou seja, B tem n linhas e p colunas)
        # A (m = 2 e n = 3) e B (n = 3 e p = 2)
        """
        A = [
            [1, 2, 3],
            [4, 5, 6]
        ]
        
        B = [
            [7, 8],
            [9, 10],
            [11, 12]
        ]
        
        AxB = [
            [1*7 + 2*9 + 3*11, 1*8 + 2*10  + 3*12],
            [4*7 + 5*9 + 6*11, 4*8 + 5*10 + 6*12]
        ]
        
        """

        return "oi"