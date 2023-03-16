from chesslexer import ChessLexer
from chessparser import ChessParser

if __name__ == '__main__':

    inputs = []

    # Instantiate and Build the lexer
    parser = ChessParser()

    #Load the input files
    filenames = ['inputs/input1.txt'] #,'inputs/input2.txt']

    for file in filenames:
        with open(file,'r') as data:
            inputs.append(data.read())

    for index, currentInput in enumerate(inputs):
        parser.test(currentInput, filenames[index])
