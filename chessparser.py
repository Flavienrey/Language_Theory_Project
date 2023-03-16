import ply.yacc as yacc
from chesslexer import tokens

class ChessParser(object):
    def p_expression_plus(self, p):
        'expression : expression PLUS term'
        p[0] = p[1] + p[3]

    def p_expression_minus(self, p):
        'expression : expression MINUS term'
        p[0] = p[1] - p[3]

    def p_expression_term(self, p):
        'expression : term'
        p[0] = p[1]

    def p_term_times(self, p):
        'term : term TIMES factor'
        p[0] = p[1] * p[3]

    def p_term_div(self, p):
        'term : term DIVIDE factor'
        p[0] = p[1] / p[3]

    def p_term_factor(self, p):
        'term : factor'
        p[0] = p[1]

    def p_factor_num(self, p):
        'factor : NUMBER'
        p[0] = p[1]

    def p_factor_expr(self, p):
        'factor : LPAREN expression RPAREN'
        p[0] = p[2]

    # Error rule for syntax errors
    def p_error(self, p):
        print("Syntax error in input!")

    # Instantiate the class and build the lexer
    def __init__(self):
        self.syntactic_error = None

        # Build the parser
        self.parser = yacc.yacc(object=self)

    def test(self, text, filename):

        print("\n=== [Current file tested :", filename, "] ===")

        result = self.parser.parse(text)
        print(result)

        # Final test to print if an error was found or not
        if self.syntactic_error:
            print("=== [File", filename, "is NOT valid, syntactic error occurred!!!] ===")
        else:
            print("=== [File", filename, "syntax is valid!] ===")