import ply.lex as lex

# List of token names.
tokens = ['NAME', 'NUMBER', 'PLUS', 'MINUS',
          'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN']

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'


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
