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
        self.error = True


    # Instantiate the class and build the lexer
    def __init__(self):
        self.error = False
        self.lexer = lex.lex(object=self)


    # Feeds the text into the lexer
    def input(self, text):
        self.lexer.input(text)


    # Returns the next token in the lexer
    def token(self):
        return self.lexer.token()


    # Test the input
    def test(self, text, filename):

        self.error = False

        print("\n=== [Current file tested :", filename,"] ===")

        self.input(text)

        for current_token in self.lexer:
            print(current_token)

        if self.error:
            print("=== [File", filename ,"is NOT valid !!!] ===")
        else:
            print("=== [File", filename ,"is valid!] ===")


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