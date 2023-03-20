from ply import yacc
from chessparser import test

# List of token names
tokens = ['TURN_NUMBER_WITH_DOT', 'TURN_AFTER_COMMENT', 'PIECE', 'MOVE', 'RESULT', 'COMMENT', 'CHECK', 'CHECKMATE',
                       'DESCRIPTION', 'GRADE', 'CASTLING', 'NEW_LINE']

if __name__ == '__main__':

    inputs = []

    # Load the input files
    filenames = ['inputs/input3.txt']  # ,'inputs/input2.txt']

    for file in filenames:
        with open(file, 'r') as data:
            inputs.append(data.read())

    # Build the parser
    parser = yacc.yacc(debug=True)

    for index, currentInput in enumerate(inputs):
        test(parser, currentInput, filenames[index])
