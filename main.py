import ply.lex as lex

# List of token names.
tokens = ['TURN', 'TURNAFTERCOMMENT', 'PIECE', 'MOVE', 'RESULT', 'COMMENT', 'CHECK', 'CHECKMATE', 'DESCRIPTION',
          'GRADE', 'CASTLING']

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


# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# feeds a string into the lexer
lexer.input("x = 3 * 4 + 5 * 6")
while True:

    # returns the next token or none.
    tok = lexer.token()

    if not tok:
        break

    # Use token
