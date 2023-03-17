import ply.lex as lex

# List of token names
tokens = ['TURN_NUMBER_WITH_DOT', 'TURN_AFTER_COMMENT', 'PIECE', 'MOVE', 'RESULT', 'COMMENT', 'CHECK', 'CHECKMATE',
                       'DESCRIPTION', 'GRADE', 'CASTLING', 'IGNORE_FILE_COMMENT', 'NEW_LINE']
class ChessLexer(object):

    # Regular expression rules for simple tokens
    t_TURN_NUMBER_WITH_DOT = r'[1-9][0-9]*\.'
    t_TURN_AFTER_COMMENT = r'[1-9][0-9]*\.{3}'
    t_PIECE = r'[P|N|B|R|Q|K]'
    t_MOVE = r'[a-h]?[1-8]?[x]?[a-h][1-8]'
    t_RESULT = r'1\-0|0\-1|1\/2\-1\/2'
    t_COMMENT = r'\{.*\}|\(.*\)'
    t_CHECK = r'[+]'
    t_CHECKMATE = r'[+][+]'
    t_DESCRIPTION = r'\[[a-zA-Z0-9_]*\s\".*\"\]'
    t_GRADE = r'[\?|\!]'
    t_CASTLING = r'O\-O(\-O)?'

    # A Comment that should be ignored
    t_IGNORE_FILE_COMMENT = r'\#.*'

    # A string containing ignored characters (spaces and tabs)
    t_ignore = ' \t'

    # Define a rule so we can track line numbers
    def t_NEW_LINE(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # Error handling rule
    def t_error(self, t):
        print("Illegal character '%s' at line %d" % (t.value[0] ,t.lexer.lineno) )
        t.lexer.skip(1)
        self.lexical_error = True


    # Instantiate the class and build the lexer
    def __init__(self):
        self.tokens = ['TURN_NUMBER_WITH_DOT', 'TURN_AFTER_COMMENT', 'PIECE', 'MOVE', 'RESULT', 'COMMENT', 'CHECK', 'CHECKMATE',
              'DESCRIPTION', 'GRADE', 'CASTLING', 'IGNORE_FILE_COMMENT', 'NEW_LINE']
        self.lexical_error = False
        self.lexer = lex.lex(object=self)


    # Feeds the text into the lexer
    def raw_input(self, text):
        self.lexer.input(text)


    # Returns the next token in the lexer
    def token(self):
        return self.lexer.token()


    # Test the input
    def input(self, text):

        # Variables initialization
        self.lexical_error = False
        self.lexer.input(text)

        print("\n[Lexical analysis started]\n")

        # We iterate over the input to read tokens
        for current_token in self.lexer:
            print(current_token)


        # Final test to print if an error was found or not
        if self.lexical_error:
            print("\n[Error during the lexical analysis]\n")
        else:
            print("\n[Correct lexical analysis]\n")
