'''
This file will contain functions for matrix operations

letterMatrix(int_x, int_y)
    returns a matrix with size x*y

printMatrix(m)
    prints the Matrix m

addWord(int_x, int_y, bool_horizontal, string_word, matrix)
    returns new matrix if successful, otherwise None
'''
#from array import *
from array import array


# a string which will be represented as empty space
EMPTY_CELL = '.'

def letterMatrix(sizeX, sizeY):
    '''
    we will create a list of arrays, constrained to characters
    '''
    matrix = []         #defining the list

    while sizeX > 0:
        column = array('c', EMPTY_CELL * sizeY)   #a row with 0 in each column
        matrix.append(column)
        sizeX -= 1

    return matrix


def printMatrix(matrix):
    '''
    this prints the contents of the matrix in a terminal
    '''
    columnLength = len(matrix[0])  #we will assume all the columns have the same length
    rowLength = len(matrix)


    y = 0
    while y < columnLength:
        x = 0
        while x < rowLength:
            print matrix[x][y],
            x += 1


        print '\n',
        y  += 1

def addWord(x, y, hor, word, m):
    '''
    x :: x-coordinate
    y :: y-coordinate
    hor :: horizontal or not
    word :: word to write
    m :: matrix to test and write

    returns False if it doesn't work, otherwise a new matrix
    '''
    if testNewWord(x,y,hor,word,m) != True:
        return False


    matrix = m
    i = 0
    j = len(word)


    #write if horizontal
    if hor:
        while i < j:
            matrix[x+i][y] = word[i]
            i += 1

    #assume it's horizontal now
    else:
        while i < j:
            matrix[x][y+i] = word[i]
            i += 1

    return matrix


def testNewWord(x, y, hor, word, matrix):
    i = 0
    j = len(word)

    if hor:
        if x + j > len(matrix):
            return False

        while i < j:
            a = matrix[x+i][y]
            b = word[i]

            #if empty, check surrounding spaces
            if a == EMPTY_CELL:
                #checking above
                if y != 0 and matrix[x+i][y-1] != EMPTY_CELL:
                    return False
                #checking beneath
                if y+1 != len(matrix[0]) and matrix[x+i][y+1] != EMPTY_CELL:
                    return False

            #else, check if it's the same
            elif a != b:
                return False

            i += 1

    #now checking vertical
    else:
        if y + j > len(matrix[0]):
            return False

        while i < j:
            a = matrix[x][y+i]
            b = word[i]

            #if empty, check surrounding spaces
            if a == EMPTY_CELL:
                #checking to the left
                if x != 0 and matrix[x-1][y+i] != EMPTY_CELL:
                    return False
                #checking beneath
                if x+1 != len(matrix) and matrix[x+1][y+i] != EMPTY_CELL:
                    return False

            #else, check if it's the same
            elif a != b:
                return False

            i += 1

    #everything looks fine
    return True