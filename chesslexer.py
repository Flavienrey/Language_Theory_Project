import ply.lex as lex

# List of token names
tokens = ['TURN_NUMBER_WITH_DOT', 'TURN_AFTER_COMMENT', 'PIECE', 'MOVE', 'RESULT', 'OPENING_PARENTHESIS', 'CLOSING_PARENTHESIS', 'OPENING_BRACE', 'CLOSING_BRACE', 'CHECK', 'CHECKMATE',
                       'DESCRIPTION', 'GRADE', 'CASTLING', 'TEXT']

class ChessLexer(object):


# A string containing ignored characters (spaces and tabs)
    t_ignore = ' \t'

    # Regular expression rules for simple tokens
   # t_TURN_NUMBER_WITH_DOT = r'[1-9][0-9]*\.'
    #t_TURN_AFTER_COMMENT = r'[1-9][0-9]*\.{3}'
    #t_PIECE = r'[P|N|B|R|Q|K]'
    #t_MOVE = r'[a-h]?[1-8]?[x]?[a-h][1-8]'
    #t_RESULT = r'1\-0|0\-1|1\/2\-1\/2'
    #t_OPENING_PARENTHESIS = r'\('
    #t_CLOSING_PARENTHESIS = r'\)'
    #t_OPENING_BRACE = r'\{'
    #t_CLOSING_BRACE = r'\}'
    #t_CHECK = r'[+]'
    #t_CHECKMATE = r'[+][+]'
    #t_DESCRIPTION = r'\[[a-zA-Z0-9_]*\s\".*\"\]'
    #t_GRADE = r'[\?|\!]'
    #t_CASTLING = r'O\-O(\-O)?'
    #t_TEXT = r'[a-zA-Z0-9_\-\.]'

    def t_TURN_NUMBER_WITH_DOT(self,t):
        r'[1-9][0-9]*\.'
        print("Token : ",t.type, "  value : ", t.value, " at line ", t.lexer.lineno)

    def t_TURN_AFTER_COMMENT(self,t):
        r'[1-9][0-9]*\.{3}'
        print("Token : ",t.type, "  value : ", t.value, " at line ", t.lexer.lineno)

    def t_PIECE(self,t):
        r'[P|N|B|R|Q|K]'
        print("Token : ",t.type, "  value : ", t.value, " at line ", t.lexer.lineno)

    def t_MOVE(self,t):
        r'[a-h]?[1-8]?[x]?[a-h][1-8]'
        print("Token : ",t.type, "  value : ", t.value, " at line ", t.lexer.lineno)

    def t_RESULT(self,t):
        r'1\-0|0\-1|1\/2\-1\/2'
        print("Token : ",t.type, "  value : ", t.value, " at line ", t.lexer.lineno)

    def t_OPENING_PARENTHESIS(self,t):
        r'\('
        print("Token : ",t.type, "  value : ", t.value, " at line ", t.lexer.lineno)

    def t_CLOSING_PARENTHESIS(self,t):
        r'\)'
        print("Token : ",t.type, "  value : ", t.value, " at line ", t.lexer.lineno)

    def t_OPENING_BRACE(self,t):
        r'\{'
        print("Token : ",t.type, "  value : ", t.value, " at line ", t.lexer.lineno)

    def t_CLOSING_BRACE(self,t):
        r'\}'
        print("Token : ",t.type, "  value : ", t.value, " at line ", t.lexer.lineno)

    def t_CHECK(self,t):
        r'[+]'
        print("Token : ",t.type, "  value : ", t.value, " at line ", t.lexer.lineno)

    def t_CHECKMATE(self,t):
        r'[+][+]'
        print("Token : ",t.type, "  value : ", t.value, " at line ", t.lexer.lineno)

    def t_DESCRIPTION(self,t):
        r'\[[a-zA-Z0-9_]*\s\".*\"\]'
        print("Token : ",t.type, "  value : ", t.value, " at line ", t.lexer.lineno)

    def t_GRADE(self,t):
        r'[\?|\!]'
        print("Token : ",t.type, "  value : ", t.value, " at line ", t.lexer.lineno)

    def t_CASTLING(self,t):
        r'O\-O(\-O)?'
        print("Token : ",t.type, "  value : ", t.value, " at line ", t.lexer.lineno)

    def t_TEXT(self,t):
        r'[a-zA-Z0-9_\-\.\'\%\,\;\:]+'
        print("Token : ",t.type, "  value : ", t.value, " at line ", t.lexer.lineno)



    # Define a rule so we can track line numbers
    def t_NEW_LINE(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # Error handling rule
    def t_error(self, t):
        self.tab_errors.append("Illegal character '%s' at line %d" % (t.value[0] ,t.lexer.lineno))
        t.lexer.skip(1)
        self.lexical_error = True


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
        print("in raw_input")


    # Returns the next token in the lexer
    def token(self):
        print("in token function", self.lexer.token())
        return self.lexer.token()


    # Test the input
    def input(self, text):

        # Variables initialization
        self.lexical_error = False
        self.lexer.input(text)

        print("\n[Lexical analysis started]")

        # We iterate over the input to read tokens
        for current_token in self.lexer:
            print("here")
            print(current_token)


        # Final test to print if an error was found or not
        if self.lexical_error:

            print("\n!!! [List of errors] !!!")

            for error in self.tab_errors:
                print('\033[91m'+error+'\033[0m')

            print("[Error during the lexical analysis]\n")

        else:
            print("[Correct lexical analysis]\n")

        # Add the input again for the parser to execute correctly
        self.lexer.input(text)
        self.lexer.lineno = 1
