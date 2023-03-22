import sys
from ply import yacc
from chessparser import *

# List of token names
tokens = ['TURN_NUMBER_WITH_DOT', 'TURN_AFTER_COMMENT', 'PIECE', 'MOVE', 'RESULT', 'COMMENT', 'CHECK', 'CHECKMATE',
                       'DESCRIPTION', 'GRADE', 'CASTLING']

if __name__ == '__main__':
    filenames = []
    #Sys.argv are all arguments given to the script
    # first argument is the script
    # the other arguments must be the names of the files to check

    if(len(sys.argv)==1):
        #no file given, we check our file test
        filenames = ['inputs/input1.txt']  # ,'inputs/input2.txt']
        print("No file given, by default we check input1.txt")
    else:
        #Load the input files
        #The file names are given, we have to format them so that our parser can find them
        for name in sys.argv[1:]:
            filenames.append('inputs/'+name)

    inputs = []
    # Build all the inputs data
    for file in filenames:
        with open(file, 'r') as data:
            inputs.append(data.read())

    # Build the parser
    parser = yacc.yacc(debug=True)

    for index, currentInput in enumerate(inputs):
        test(parser, currentInput, filenames[index])
