import ply.yacc as yacc
from chesslexer import tokens, ChessLexer

def p_game(p):
    '''game : eventDescriptor turn RESULT game
            | empty'''

def p_event_descriptor(p):
    '''eventDescriptor : DESCRIPTION NEW_LINE eventDescriptor
            | empty'''

def p_turn(p):
    '''turn : TURN_NUMBER_WITH_DOT whiteMove eventGrade whiteComment blackMove eventGrade blackComment  turn
            | empty'''

def p_event_grade(p):
    '''eventGrade : GRADE
            | empty'''

def p_white_move(p):
    '''whiteMove : PIECE MOVE eventCheck eventCheckMate
            | CASTLING'''

def p_black_move(p):
    '''blackMove : PIECE MOVE eventCheck eventCheckMate
            | CASTLING
            | empty'''

def p_event_check(p):
    '''eventCheck : CHECK
            | empty'''

def p_event_check_mate(p):
    '''eventCheckMate : CHECKMATE
            | empty'''

def p_white_comment(p):
    '''whiteComment : COMMENT TURN_AFTER_COMMENT
            | empty'''

def p_black_comment(p):
    '''blackComment : COMMENT
            | empty'''


# Empty production
def p_empty(p):
    '''empty :'''
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

