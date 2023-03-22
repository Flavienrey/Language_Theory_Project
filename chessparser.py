from ply import yacc
from chesslexer import ChessLexer
from node import Node

# List of token names
tokens = ['TURN_NUMBER_WITH_DOT', 'TURN_AFTER_COMMENT', 'PIECE', 'MOVE', 'RESULT', 'COMMENT', 'CHECK', 'CHECKMATE',
          'DESCRIPTION', 'GRADE', 'CASTLING']

syntactic_error = None
tab_errors = []
tree = None
turnIndex = None
parser = None

def get_elem_in_slice(p, index):
    if index < len(p.slice):
        return p.slice[index]
    return None


def p_start(p):
    '''start : game'''
    global tree
    tree = Node(get_elem_in_slice(p, 1))


def p_game(p):
    '''game : eventDescriptor turn RESULT game
            | empty'''
    p[0] = Node([get_elem_in_slice(p, 1), get_elem_in_slice(p, 2), get_elem_in_slice(p, 3), get_elem_in_slice(p, 4)])


def p_event_descriptor(p):
    '''eventDescriptor : DESCRIPTION eventDescriptor
                       | empty'''

    p[0] = Node([get_elem_in_slice(p, 1), get_elem_in_slice(p, 2)])


def p_turn(p):
    '''turn : empty
            | TURN_NUMBER_WITH_DOT whiteMove eventGrade whiteComment blackMove eventGrade blackComment  turn'''


    global turnIndex, tab_errors, syntactic_error

    current_turn = get_elem_in_slice(p, 1)

    if current_turn.value is not None:

        if turnIndex is None:
            turnIndex = int(current_turn.value.split('.')[0])

        if current_turn.value == str(turnIndex)+'.':
            p[0] = Node([get_elem_in_slice(p, 1), get_elem_in_slice(p, 2), get_elem_in_slice(p, 3), get_elem_in_slice(p, 4),
                     get_elem_in_slice(p, 5), get_elem_in_slice(p, 6), get_elem_in_slice(p, 7), get_elem_in_slice(p, 8)])

        else:

            string_error = "Error : Should be turn "+str(turnIndex)+" and is turn "+ str(current_turn.value)
            tab_errors.append(string_error)
            syntactic_error = True

        turnIndex -= 1

    else:
        turnIndex = None


def p_event_grade(p):
    '''eventGrade : GRADE
                  | empty'''
    p[0] = Node(get_elem_in_slice(p, 1))


def p_white_move(p):
    '''whiteMove : eventPiece MOVE eventCheck
                 | CASTLING'''
    p[0] = Node([get_elem_in_slice(p, 1), get_elem_in_slice(p, 2), get_elem_in_slice(p, 3)])


def p_black_move(p):
    '''blackMove : eventPiece MOVE eventCheck
                 | CASTLING
                 | empty'''
    p[0] = Node([get_elem_in_slice(p, 1), get_elem_in_slice(p, 2), get_elem_in_slice(p, 3)])


def p_event_piece(p):
    '''eventPiece : PIECE
                | empty'''
    p[0] = Node(get_elem_in_slice(p, 1))


def p_event_check(p):
    '''eventCheck : CHECK
                  | CHECKMATE
                  | empty'''
    p[0] = Node(get_elem_in_slice(p, 1))


def p_white_comment(p):
    '''whiteComment : COMMENT TURN_AFTER_COMMENT
                    | empty'''
    p[0] = Node([get_elem_in_slice(p, 1), get_elem_in_slice(p, 2)])


def p_black_comment(p):
    '''blackComment : COMMENT
                    | empty'''
    p[0] = Node(get_elem_in_slice(p, 1))


# Empty production
def p_empty(p):
    '''empty :'''
    p[0] = None


# Error rule for syntax errors
def p_error(p):

    global parser

    if p:
        global syntactic_error
        global tab_errors
        syntactic_error = True
        tab_errors.append("Syntax error : " + p.type + ", " + p.value + " at line " + str(p.lineno))
        parser.errok()
    else:
        print("Syntax error at EOF")


def test(text, filename):

    global syntactic_error, tab_errors, tree, turnIndex, parser

    # Build the parser
    parser = yacc.yacc(debug=True)
    syntactic_error = None
    tab_errors = []
    tree = None
    turnIndex = None

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
        print("[Correct syntactic analysis]")

    print("\n=== [File", filename, "verifications is done!] ===")

    return tree
