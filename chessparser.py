import ply.yacc as yacc
from chesslexer import tokens, ChessLexer

def p_game(p):
    'game : eventDescriptor turn gameResults game'
    '     | empty'

def p_event_descriptor(p):
    'eventDescriptor : DESCRIPTION newline eventDescriptor'
    '     | empty'

def p_turn(p):
    'turn : TURN whiteMove whiteComment blackMove blackComment turn'
    '     | empty'

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
        self.tab_errors =[]
        # Build the parser
        self.parser = yacc.yacc()

    def test(self, text, filename):
        print("\n=== [Current file tested :", filename, "] ===")
        lexer = ChessLexer()
        result = self.parser.parse(text, lexer=lexer)
        print("\n[Syntaxic analysis started]\n")
        # Final test to print if an error was found or not
        if self.syntactic_error:
            print("\n[Error during the syntaxic analysis] :")
            for error in self.tab_errors:
                print(error)
        else:
            print("\n[Correct syntaxic analysis]\n")

        print("\nResult :", result)
        print("\n=== [File", filename, "verifications is done!] ===")

