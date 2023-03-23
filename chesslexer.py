import ply.lex as lex
from colors import Colors

# List of token names
tokens = ['TURN_NUMBER_WITH_DOT', 'TURN_AFTER_COMMENT', 'PIECE', 'MOVE', 'RESULT', 'OPENING_PARENTHESIS', 'CLOSING_PARENTHESIS', 'OPENING_BRACE', 'CLOSING_BRACE', 'CHECK', 'CHECKMATE',
                       'DESCRIPTION', 'GRADE', 'CASTLING', 'TEXT']

class ChessLexer(object):


# A string containing ignored characters (spaces and tabs)
    t_ignore = ' \t'

    def t_TURN_AFTER_COMMENT(self, t):
        r'[1-9][0-9]*\.{3}'
        print("Token : ", t.type, "  value : ", t.value, " at line ", t.lexer.lineno)
        return t

    def t_TURN_NUMBER_WITH_DOT(self,t):
        r'[1-9][0-9]*\.'
        print("Token : ",t.type, "  value : ", t.value, " at line ", t.lexer.lineno)
        return t

    def t_PIECE(self,t):
        r'[P|N|B|R|Q|K]'
        print("Token : ",t.type, "  value : ", t.value, " at line ", t.lexer.lineno)
        return t

    def t_MOVE(self,t):
        r'[a-h]?[1-8]?[x]?[a-h][1-8]'
        print("Token : ",t.type, "  value : ", t.value, " at line ", t.lexer.lineno)
        return t

    def t_RESULT(self,t):
        r'1\-0|0\-1|1\/2\-1\/2'
        print("Token : ",t.type, "  value : ", t.value, " at line ", t.lexer.lineno)
        return t

    def t_OPENING_PARENTHESIS(self,t):
        r'\('
        print("Token : ",t.type, "  value : ", t.value, " at line ", t.lexer.lineno)
        return t

    def t_CLOSING_PARENTHESIS(self,t):
        r'\)'
        print("Token : ",t.type, "  value : ", t.value, " at line ", t.lexer.lineno)
        return t

    def t_OPENING_BRACE(self,t):
        r'\{'
        print("Token : ",t.type, "  value : ", t.value, " at line ", t.lexer.lineno)
        return t

    def t_CLOSING_BRACE(self,t):
        r'\}'
        print("Token : ",t.type, "  value : ", t.value, " at line ", t.lexer.lineno)
        return t

    def t_CHECKMATE(self,t):
        r'[+][+]'
        print("Token : ",t.type, "  value : ", t.value, " at line ", t.lexer.lineno)
        return t

    def t_CHECK(self,t):
        r'[+]'
        print("Token : ",t.type, "  value : ", t.value, " at line ", t.lexer.lineno)
        return t

    def t_DESCRIPTION(self,t):
        r'\[[a-zA-Z0-9_]*\s\".*\"\]'
        print("Token : ",t.type, "  value : ", t.value, " at line ", t.lexer.lineno)
        return t

    def t_GRADE(self,t):
        r'[\?|\!]'
        print("Token : ",t.type, "  value : ", t.value, " at line ", t.lexer.lineno)
        return t

    def t_CASTLING(self,t):
        r'O\-O(\-O)?'
        print("Token : ",t.type, "  value : ", t.value, " at line ", t.lexer.lineno)
        return t

    def t_TEXT(self,t):
        r'[a-zA-Z0-9_\-\.\'\%\,\;\:]+'
        print("Token : ",t.type, "  value : ", t.value, " at line ", t.lexer.lineno)
        return t

    # Define a rule so we can track line numbers
    def t_NEW_LINE(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # Error handling rule
    def t_error(self, t):
        error = "Illegal character '%s' at line %d" % (t.value[0] ,t.lexer.lineno)
        print(Colors.FAIL + error + Colors.ENDC)
        t.lexer.skip(1)


    # Instantiate the class and build the lexer
    def __init__(self):
        self.tokens = ['TURN_NUMBER_WITH_DOT', 'TURN_AFTER_COMMENT', 'PIECE', 'MOVE', 'RESULT',  'OPENING_PARENTHESIS',
                       'CLOSING_PARENTHESIS', 'OPENING_BRACE', 'CLOSING_BRACE', 'CHECK', 'CHECKMATE', 'DESCRIPTION', 'GRADE', 'CASTLING', 'TEXT',]
        self.lexical_error = False
        self.lexer = lex.lex(object=self)
        self.tab_errors = []


    # Feeds the text into the lexer
    def raw_input(self, text):
        self.lexer.input(text)


    # Returns the next token in the lexer
    def token(self):
        return self.lexer.token()


    # Test the input
    def input(self, text):

        self.lexer.input(text)

        # Add the input again for the parser to execute correctly
        self.lexer.input(text)
        self.lexer.lineno = 1
