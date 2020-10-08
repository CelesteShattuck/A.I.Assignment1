#Simple function to find the empty space in our puzzle
#we just require the actual matrix we are working with


def main(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if matrix[i][j] == 0: return i, j