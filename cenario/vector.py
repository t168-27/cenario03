class Vector:
    """
    Classe que representa um vetor. Cria por padrão um vetor linha.

    Attributes
    -------
    dim (int): Dimensão do vetor.
    elements (list): Lista dos elementos do vetor.
    rows (int): Número de linhas do vetor.
    cols (int): Número de colunas do vetor.
    """
    def __init__(self, dim: int, elements: [int]):
        """
        Inicializa a classe Vector.

        Parâmetros:
        dim (int): Dimensão do vetor.
        elements (list): Lista dos elementos do vetor.
        """
        self.dim = dim
        self.elements = elements
        self.rows = 1
        self.cols = len(elements)

    def __repr__(self) -> str:
        return '[' + '\n '.join([repr(self.elements[((line-1) * self.cols):(self.cols * line)]) for line in range(1, self.rows + 1)]) + ']'

    def get(self, i: int) -> int:
        """
        Obtém o valor de um elemento específico de um objeto de tipo Vector.

        Parameters
        ----------
        i (int): O índice do elemento (começando em 1).

        Returns
        -------
        int: O valor do elemento na posição i.
        """
        return self.elements[i-1]

    def set(self, i: int, value: int) -> int:
        """
        Atribui um valor a um elemento específico de um objeto de tipo Vector.

        Parameters
        ----------
        i (int): O índice do elemento (começando em 1).
        value (int): O novo valor a ser atribuído ao elemento.

        Returns
        -------
        int: O valor atribuído ao elemento.
        """
        self.elements[i-1] = value