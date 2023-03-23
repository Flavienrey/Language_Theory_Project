from ply import yacc
from chesslexer import ChessLexer
from node import Node

# List of token names
tokens = ['TURN_NUMBER_WITH_DOT', 'TURN_AFTER_COMMENT', 'PIECE', 'MOVE', 'RESULT', 'OPENING_PARENTHESIS', 'CLOSING_PARENTHESIS', 'OPENING_BRACE', 'CLOSING_BRACE', 'CHECK', 'CHECKMATE',
                       'DESCRIPTION', 'GRADE', 'CASTLING', 'TEXT']

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
            | TURN_NUMBER_WITH_DOT whiteMove eventGrade whiteComment blackMove eventGrade simpleComment  turn'''

    global turnIndex, tab_errors, syntactic_error

    current_turn = get_elem_in_slice(p, 1)

    if current_turn.value is not None:

        if turnIndex is None:
            turnIndex = int(current_turn.value.split('.')[0])

        if current_turn.value != str(turnIndex) + '.':
            string_error = "Turn " + str(turnIndex) + " missing"
            tab_errors.append(string_error)
            syntactic_error = True
            turnIndex -= 1

        else:
            p[0] = Node(
                [get_elem_in_slice(p, 1), get_elem_in_slice(p, 2), get_elem_in_slice(p, 3), get_elem_in_slice(p, 4),
                 get_elem_in_slice(p, 5), get_elem_in_slice(p, 6), get_elem_in_slice(p, 7), get_elem_in_slice(p, 8)])

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
    '''whiteComment : openingCharacter eventData simpleComment eventData closingCharacter TURN_AFTER_COMMENT
                    | empty'''

    # check if opening == closing
    p[0] = Node([get_elem_in_slice(p, 1), get_elem_in_slice(p, 2)])


def p_simple_comment(p):
    '''simpleComment : openingCharacter eventData simpleComment eventData closingCharacter
                     | empty'''
    # check if opening == closing
    p[0] = Node(get_elem_in_slice(p, 1))

def p_event_data(p):
    '''eventData : TURN_NUMBER_WITH_DOT eventData
                 | TURN_AFTER_COMMENT eventData
                 | PIECE eventData
                 | MOVE eventData
                 | RESULT eventData
                 | TEXT eventData
                 | CHECK eventData
                 | CHECKMATE eventData
                 | GRADE eventData
                 | CASTLING eventData
                 | empty'''

def p_opening_character(p):
    '''openingCharacter : OPENING_PARENTHESIS
                        | OPENING_BRACE'''

def p_closing_character(p):
    '''closingCharacter : CLOSING_PARENTHESIS
                        | CLOSING_BRACE'''


# Empty production
def p_empty(p):
    '''empty :'''
    p[0] = None


# Error rule for syntax errors
def p_error(p):
    global parser

    if p:
        global syntactic_error, tab_errors, parser
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

    return tree, tab_errors
