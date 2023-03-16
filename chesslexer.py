import ply.lex as lex
class ChessLexer(object):

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
    t_DESCRIPTION = r'\[[a-zA-Z0-9_]*\s\".*\"\]'
    t_GRADE = r'[\?|\!]'
    t_CASTLING = r'O\-O(\-O)?'

    # A Comment that should be ignored
    t_IGNORE_FILE_COMMENT = r'\#.*'

    # A string containing ignored characters (spaces and tabs)
    t_ignore = ' \t'

    # Define a rule so we can track line numbers
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # Error handling rule
    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
        self.lexical_error = True


    # Instantiate the class and build the lexer
    def __init__(self):
        self.previous_token = None
        self.syntactic_error = None
        self.lexical_error = False
        self.lexer = lex.lex(object=self)


    # Feeds the text into the lexer
    def input(self, text):
        self.lexer.input(text)


    # Returns the next token in the lexer
    def token(self):
        return self.lexer.token()


    # Test the input
    def test(self, text, filename):

        # Variables initialization
        self.lexical_error = False
        self.input(text)

        print("\n=== [Current file tested :", filename,"] ===")

        # We iterate over the input to read tokens
        for current_token in self.lexer:
            print(current_token)


        # Final test to print if an error was found or not
        if self.lexical_error:
            print("=== [File", filename ,"is NOT valid, there is a lexical error!!!] ===")
        else:
            print("=== [File", filename ,"is valid, no lexical error occurred!] ===")