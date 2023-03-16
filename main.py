from chesslexer import ChessLexer

if __name__ == '__main__':

    inputs = []

    # Instantiate and Build the lexer
    lexer = ChessLexer()

    #Load the input files
    filenames = ['inputs/input1.txt','inputs/input2.txt']

    for file in filenames:
        with open(file,'r') as data:
            inputs.append(data.read())

    for index, currentInput in enumerate(inputs):

        lexer.test(currentInput, filenames[index])
