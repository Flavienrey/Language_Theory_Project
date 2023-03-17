import ply.yacc as yacc
from chesslexer import tokens, ChessLexer
from node import Node

def p_start(p):
    '''start : game'''
    print("see")

def p_game(p):
    '''game : eventDescriptor turn RESULT game
            | empty'''
    print("see")

def p_event_descriptor(p):
    '''eventDescriptor : DESCRIPTION NEW_LINE eventDescriptor
                       | empty'''
    print("see")

def p_turn(p):
    '''turn : TURN_NUMBER_WITH_DOT whiteMove eventGrade whiteComment blackMove eventGrade blackComment  turn
            | empty'''
    print("see")

def p_event_grade(p):
    '''eventGrade : GRADE
                  | empty'''
    print("see")

def p_white_move(p):
    '''whiteMove : PIECE MOVE eventCheck
                 | CASTLING'''
    print("see")

def p_black_move(p):
    '''blackMove : PIECE MOVE eventCheck
                 | CASTLING
                 | empty'''
    print("see")

def p_event_check(p):
    '''eventCheck : CHECK
                  | CHECKMATE
                  | empty'''
    print("see")


def p_white_comment(p):
    '''whiteComment : COMMENT TURN_AFTER_COMMENT
                    | empty'''
    print("see")

def p_black_comment(p):
    '''blackComment : COMMENT
                    | empty'''
    print("see")


# Empty production
def p_empty(p):
    '''empty :'''
    pass


class ChessParser(object):

    # Error rule for syntax errors
    def p_error(self, p):
        if p:
            print("Syntax error at token", p.type)
            # Just discard the token and tell the parser it's okay.
            self.parser.errok()
        else:
            print("Syntax error at EOF")

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

