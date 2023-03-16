import ply.yacc as yacc
from chesslexer import tokens, ChessLexer

# Empty production
def p_empty(p):
    'empty :'
    pass

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

class ChessParser(object):

    # Instantiate the class and build the parser
    def __init__(self):
        self.syntactic_error = None
        self.tokens = tokens
        # Build the parser
        self.parser = yacc.yacc()

    def test(self, text, filename):

        print("\n=== [Current file tested :", filename, "] ===")

        lexer = ChessLexer()

        result = self.parser.parse(text, lexer=lexer)

        print("Result :", result)

        print("=== [File", filename, "verifications is done!] ===")

