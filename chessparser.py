import ply.yacc as yacc
from chesslexer import tokens

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1]

# Error rule for syntax errors
    def p_error(self):
        print("Syntax error in input!")

class ChessParser(object):

    # Instantiate the class and build the lexer
    def __init__(self):
        self.syntactic_error = None
        self.tokens = tokens
        # Build the parser
        self.parser = yacc.yacc()

    def test(self, text, filename):

        print("\n=== [Current file tested :", filename, "] ===")

        result = self.parser.parse(text)
        print(result)

        # Final test to print if an error was found or not
        if self.syntactic_error:
            print("=== [File", filename, "is NOT valid, syntactic error occurred!!!] ===")
        else:
            print("=== [File", filename, "syntax is valid!] ===")