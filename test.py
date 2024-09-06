from cenario import LinearAlgebra, _matrix_to_columns, _matrix_to_lines
from cenario.matrix import Matrix
from copy import deepcopy
# a = Matrix(2, 2, [1, 5, -2, 2])

# print(LinearAlgebra._determinant(a))
# print(LinearAlgebra._determinant(LinearAlgebra().transpose(a)))


e = [11,12,13,21,22,23,31,32,33]
m = Matrix(3, 3, e)

print(m, end = '\n\n')

rows = _matrix_to_lines(m)

row_to_expand = 1

l = list(range(1, m.rows + 1))
c = list(range(1, m.cols + 1))

l.remove(row_to_expand)

for k, e in enumerate(rows[row_to_expand - 1]):
    c_submatrix = [j for j in c if j != (k + 1)]
    submatrix = Matrix(m.rows - 1, m.cols - 1, [m.get(i,j) for i in l for j in c_submatrix])
    print(submatrix)
    det = LinearAlgebra().determinant(submatrix)
    cc = ((-1) ** (row_to_expand + k + 1))
    print({'det': det, 'k': k,'row_to_expand': row_to_expand,'cc': cc})
    # cofactor =  * det


# print(LinearAlgebra().determinant(m))

# rows = _matrix_to_lines(m)
# cols = _matrix_to_columns(m)

# print(rows)
# print(cols)

# print(not all([any(row) for row in rows]))
# print(not all([any(col) for col in cols]))