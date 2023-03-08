import ply.lex as lex

# List of token names.
tokens = ['TURN', 'TURNAFTERCOMMENT', 'PIECE', 'MOVE', 'RESULT', 'COMMENT', 'CHECK', 'CHECKMATE', 'DESCRIPTION',
          'GRADE', 'CASTLING']

#TODO Test with some unit tests those regex

# Regular expression rules for simple tokens
t_TURN = r'[1-9][0-9]*\.'
t_TURNAFTERCOMMENT = r'[1-9][0-9]*\.{3}'
t_PIECE = r'[P|N|B|R|Q|K]'
t_MOVE = r'[a-h]?[1-8]?[x]?[a-h][1-8]'
t_RESULT = r'1\-0|0\-1|1\/2\-1\/2'
t_COMMENT = r'\{.*\}|\(.*\)'
t_CHECK = r'[+]'
t_CHECKMATE = r'[+][+]'
t_DESCRIPTION = r'^\[[a-zA-Z0-9_]*\s\".*\"\]\n'
t_GRADE = r'[\?|\!]'
t_CASTLING = r'O\-O(\-O)?'

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

#Load the input files
filenames = ['inputs/input1.txt','inputs/input2.txt']
inputs = []

for file in filenames:
    with open(file,'r') as data:
        inputs.append(data.read())

for index, currentInput in enumerate(inputs):

    # Printing the name of the file that is tested
    print("Current file tested : ", filenames[index])

    #TODO add a way to check if an error occurred for the file, to print file valid or not

    # Feeds a file into the lexer
    lexer.input(currentInput)
    while True:

        # Returns the next token or none.
        tok = lexer.token()

        # If end of file, we break the infinite loop
        if not tok:
            break

        # Use token
        # TODO Add code here