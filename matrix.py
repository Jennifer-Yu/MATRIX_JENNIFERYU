def print_matrix( matrix ):
    for col in range(len(matrix[0])):
        r = ""
        for row in matrix:
            r += str(row[col]) + "  "
        print r

def ident( matrix ):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if row == col:
                matrix[row][col] = 1.0
            else:
                matrix[row][col] = 0.0


def scalar_mult( matrix, s ):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            matrix[row][col] = matrix[row][col] * s

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    r1 = len(m1)
    r2 = len(m1[0])
    c1 = len(m2)
    c2 = len(m2[0])
    temp = new_matrix(r1, c2)
    for r in range(r1):
        for c in range(c2):
            for x in range(r2):
                temp[r][c] += m1[r][x] * m2[x][c]
    for row in range(c1):
        for col in range(len(m2[r])):
            m2[row][col] = temp[row][col]

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0.0 )
    return m

def new_matrix2(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 1.0 )
    return m
