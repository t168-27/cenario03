def get_element_index(row: int, col: int, n_cols: int) -> int:
    """
    Calcula o índice no atributo elements de um objeto Matrix
    que representa o elemento da matriz na linha row e coluna col.

    Parameters
    ----------
    row (int): O número da linha do elemento.
    col (int): O número da coluna do elemento.
    n_cols (int): O número total de colunas no objeto Matrix.

    Returns
    -------
    int: O índice do elemento.
    """
    return ((row-1) * n_cols) + (col-1)

class Matrix:
    """
    Classe que representa uma matriz.

    Attributes
    -------
    rows (int): Número de linhas da matriz.
    cols (int): Número de colunas da matriz.
    elements (list): Lista dos elementos da matriz, na ordem linha a linha.
    """
    def __init__(self, rows: int, cols: int, elements):
        """
        Inicializa a classe Matrix.

        Parameters
        ----------
        rows (int): Número de linhas da matriz.
        cols (int): Número de colunas da matriz.
        elements (list): Lista dos elementos da matriz.
        """
        
        if len(elements) != (rows * cols):
            raise Exception(f'Matriz {rows} X {cols} precisa de {(rows * cols)} elementos mas {len(elements)} foram fornecidos.')
        
        self.rows = rows
        self.cols = cols
        self.elements = elements
    
    def __repr__(self) -> str:
        return '[' + '\n '.join([repr(self.elements[((line-1) * self.cols):(self.cols * line)]) for line in range(1, self.rows + 1)]) + ']'

    
    def get(self, i: int, j: int) -> int:
        """
        Obtém o valor de um elemento específico de um objeto de tipo Matrix.

        Parameters
        ----------
        i (int): O número da linha do elemento.
        j (int): O número da coluna do elemento.

        Returns
        -------
        int: O valor do elemento na posição (i, j).
        """
        return self.elements[get_element_index(i, j, self.cols)]

    
    def set(self, i: int, j: int, value):
        """
        Atribui um valor a um elemento específico do objeto de tipo Matrix.

        Parameters
        ----------
        i (int): O número da linha do elemento.
        j (int): O número da coluna do elemento.
        value (int): O novo valor a ser atribuído ao elemento.
        """
        self.elements[get_element_index(i, j, self.cols)] = value