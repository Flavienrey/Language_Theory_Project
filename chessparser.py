import ply.yacc as yacc
from chesslexer import tokens

class ChessParser(object):


    def p_expression_plus(self, p):
        'expression : expression PLUS term'
        p[0] = p[1] + p[3]

    # Error rule for syntax errors
    def p_error(self):
        print("Syntax error in input!")

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