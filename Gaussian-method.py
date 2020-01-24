#http://www.mathros.net.ua/metod-gaussa-z-vyborom-golovnogo-elementa.html
#site with example which tests in program


# program  will help reduce the matrix to a triangular appearance
# for the Gaussian method with the choice of prime


def print_current_matrix(matrix): # print matrix after steps

    for x in range(len(matrix)):
        print(matrix[x])

def findMaxElement(matrix): # find find max element
    row_i = 0
    col_i = 0
    max_value = matrix[row_i][col_i]
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            if abs(matrix[x][y]) > abs(max_value):
                max_value = matrix[x][y]
                row_i = x
                col_i = y

    return max_value, row_i, col_i

def findMainRow(matrix, i): # get main row
    return matrix[i]

def multiplyElement(matrix, maxElement, i, j): # function for multiply elements and coefs

    for x in range(len(matrix)):
        if x != i:
            for y in range(len(matrix)+1):
                if y != j:
                    matrix[x][y] += -(matrix[x][j] / maxElement) * matrix[i][y]

def zeroing(matrix, i, j):  # func for zeroing elements which not zeroed by multiply step
    for x in range(len(matrix)):
        if x != i:
           matrix[x][j] = 0

def deleteLines(matrix, i, j): # func delete for delete rows and columns
        for x in matrix:
            del x[j]

        del matrix[i]
if __name__ == '__main__':

    INPUT = [
        [1, 5, 3, -4, 20],
        [3, 1, -2, 0, 9],
        [5, -7, 0, 10, -9],
        [0, 3, -5, 0, 1]
    ]
    print("INPUT MATRIX:")
    print_current_matrix(INPUT)

    for n in range(4):
        print(f"\n# STEP {n+1}: ")

        maxElement, i, j = findMaxElement(INPUT)
        print(f"# Max element :\n#", maxElement)
        print(f"# Max element`s indexes :\n#", i, j)

        mainRow = findMainRow(INPUT, i)
        print("# Main row :\n#", mainRow)

        multiplyElement(INPUT, maxElement, i, j)

        zeroing(INPUT, i, j)

        print_current_matrix(INPUT)

        deleteLines(INPUT, i, j)








