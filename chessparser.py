from chesslexer import ChessLexer

syntactic_error = None
tab_errors = []

def p_start(p):
    '''start : game'''
    #print("start")

def p_game(p):
    '''game : eventDescriptor turn RESULT game
            | empty'''
    #print("game")

def p_event_descriptor(p):
    '''eventDescriptor : DESCRIPTION eventDescriptor
                       | empty'''
    #print("eventDescriptor")

def p_turn(p):
    '''turn : TURN_NUMBER_WITH_DOT whiteMove eventGrade whiteComment blackMove eventGrade blackComment  turn
            | empty'''
    #print("turn")

def p_event_grade(p):
    '''eventGrade : GRADE
                  | empty'''
    #print("grade")

def p_white_move(p):
    '''whiteMove : eventPiece MOVE eventCheck
                 | CASTLING'''
    #print("whiteMove")

def p_black_move(p):
    '''blackMove : eventPiece MOVE eventCheck
                 | CASTLING
                 | empty'''
    #print("blackMove")

def p_event_piece(p):
    '''eventPiece : PIECE
                | empty'''
    #print("eventPiece")

def p_event_check(p):
    '''eventCheck : CHECK
                  | CHECKMATE
                  | empty'''
    #print("eventCheck")


def p_white_comment(p):
    '''whiteComment : COMMENT TURN_AFTER_COMMENT
                    | empty'''
    #print("whiteComment")

def p_black_comment(p):
    '''blackComment : COMMENT
                    | empty'''
    #print("blackComment")

# Empty production
def p_empty(p):
    '''empty :'''
    #print("empty")

# Error rule for syntax errors
def p_error(p):
    if p:
        global syntactic_error
        global tab_errors
        syntactic_error = True
        tab_errors.append("Syntax error : "+ p.type + ", " + p.value +" at line " + str(p.lineno))
    else:
        print("Syntax error at EOF")

def test(parser, text, filename):
    print("\n=== [Current file tested :", filename, "] ===")

    lexer = ChessLexer()

    parser.parse(text, lexer=lexer)

    print("[Syntactic analysis started]")

    # Final test to print if an error was found or not
    if syntactic_error:

        print("!!! [List of errors] !!!")

        for error in tab_errors:
            print('\033[91m' + error + '\033[0m')

        print("[Error during the syntactic analysis]")

    else:
        print("\n[Correct syntactic analysis]\n")

    print("\n=== [File", filename, "verifications is done!] ===")