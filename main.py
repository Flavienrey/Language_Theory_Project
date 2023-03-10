import ply.lex as lex

# List of token names.
tokens = ['TURN', 'TURN_AFTER_COMMENT', 'PIECE', 'MOVE', 'RESULT', 'COMMENT', 'CHECK', 'CHECKMATE', 'DESCRIPTION',
          'GRADE', 'CASTLING', 'IGNORE_FILE_COMMENT']

# Regular expression rules for simple tokens
t_TURN = r'[1-9][0-9]*\.'
t_TURN_AFTER_COMMENT = r'[1-9][0-9]*\.{3}'
t_PIECE = r'[P|N|B|R|Q|K]'
t_MOVE = r'[a-h]?[1-8]?[x]?[a-h][1-8]'
t_RESULT = r'1\-0|0\-1|1\/2\-1\/2'
t_COMMENT = r'\{.*\}|\(.*\)'
t_CHECK = r'[+]'
t_CHECKMATE = r'[+][+]'
t_DESCRIPTION = r'^\[[a-zA-Z0-9_]*\s\".*\"\]\n'
t_GRADE = r'[\?|\!]'
t_CASTLING = r'O\-O(\-O)?'

# A Comment that should be ignored
t_IGNORE_FILE_COMMENT = r'\#.*'

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()


#TODO add a way to check if an error occurred for the file, to print file valid or not
# Launch all test units
if __name__ == '__main__':

    inputs = []

    #Load the input files
    filenames = ['inputs/input1.txt','inputs/input2.txt']

    for file in filenames:
        with open(file,'r') as data:
            inputs.append(data.read())

    for index, currentInput in enumerate(inputs):

        print("Current file tested : ", filenames[index])

        # Feeds a file into the lexer
        lexer.input(currentInput)

        for tok in lexer:
            print(tok)