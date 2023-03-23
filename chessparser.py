from ply import yacc
from chesslexer import ChessLexer
from node import Node
from colors import Colors

# List of token names
tokens = ['TURN_NUMBER_WITH_DOT', 'TURN_AFTER_COMMENT', 'PIECE', 'MOVE', 'RESULT', 'OPENING_PARENTHESIS', 'CLOSING_PARENTHESIS', 'OPENING_BRACE', 'CLOSING_BRACE', 'CHECK', 'CHECKMATE',
                       'DESCRIPTION', 'GRADE', 'CASTLING', 'TEXT']

syntactic_error = None
tab_errors = []
tree = None
turnIndex = None
parser = None


# Function used to get an element in the tree based on its index
# Allows us to not "index out of range" if the element is not present
# Much safer overall
def get_elem_in_slice(p, index):
    if index < len(p.slice):
        return p.slice[index]
    return None


# Function used to determine at the end of the game/file if some turns have been omitted
def check_if_missing_turns_after_file():
    global turnIndex, syntactic_error

    # If turnIndex is not None or >= to 1, some turns are missing in the file
    if None != turnIndex >= 1:

        # We print each missing turn
        for i in range(1, turnIndex + 1):
            string_error = "Turn " + str(i) + " missing"
            tab_errors.append(string_error)

        # We tell the program that there is an error
        syntactic_error = True
        turnIndex = None


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

    p[0] = Node(
        [get_elem_in_slice(p, 1), get_elem_in_slice(p, 2), get_elem_in_slice(p, 3), get_elem_in_slice(p, 4),
         get_elem_in_slice(p, 5), get_elem_in_slice(p, 6), get_elem_in_slice(p, 7), get_elem_in_slice(p, 8)])

    global turnIndex, tab_errors, syntactic_error

    # We get the current TURN_NUMBER_WITH_DOT
    current_turn = get_elem_in_slice(p, 1)

    # If the TURN_NUMBER_WITH_DOT is present
    if current_turn.value is not None:

        # If we didn't start to count yet, we initialize our counter
        if turnIndex is None:
            turnIndex = int(current_turn.value.split('.')[0])

        # We iterate over the values that we need till the end of the file
        # If we get the first one, we break, otherwise we indicate its missing and continue until finding one
        for _ in range(turnIndex, -1, -1):

            # If expected turn is different from what we got, we raise an error and decrease to the next turn
            if current_turn.value != str(turnIndex) + '.':

                string_error = "Turn " + str(turnIndex) + " missing"
                tab_errors.append(string_error)
                syntactic_error = True
                turnIndex -= 1

            # Now equal to our turn, we break
            else:
                break

        # We decrement our index to check the next one next time
        turnIndex -= 1

    else:
        check_if_missing_turns_after_file()
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

    p[0] = Node([get_elem_in_slice(p, 1), get_elem_in_slice(p, 2), get_elem_in_slice(p, 3), get_elem_in_slice(p, 4),
                 get_elem_in_slice(p, 5), get_elem_in_slice(p, 6)])


def p_simple_comment(p):
    '''simpleComment : openingCharacter eventData simpleComment eventData closingCharacter
                     | empty'''
    # check if opening == closing
    p[0] = Node([get_elem_in_slice(p, 1), get_elem_in_slice(p, 2), get_elem_in_slice(p, 3), get_elem_in_slice(p, 4),
                 get_elem_in_slice(p, 5)])


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
    p[0] = Node([get_elem_in_slice(p, 1), get_elem_in_slice(p, 2)])


def p_opening_character(p):
    '''openingCharacter : OPENING_PARENTHESIS
                        | OPENING_BRACE'''
    p[0] = Node(get_elem_in_slice(p, 1))


def p_closing_character(p):
    '''closingCharacter : CLOSING_PARENTHESIS
                        | CLOSING_BRACE'''
    p[0] = Node(get_elem_in_slice(p, 1))


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
        tab_errors.append("Syntax error : " + p.type + " " + p.value + " not allowed at line " + str(p.lineno))
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

    print("=== [Current file tested :", filename, "] ===")
    print("[Analysis started]")

    lexer = ChessLexer()

    parser.parse(text, lexer=lexer)

    check_if_missing_turns_after_file()

    # Final test to print if an error was found or not
    if syntactic_error:

        for error in tab_errors:
            print(Colors.FAIL + error + Colors.ENDC)

        print(Colors.WARNING + "[Error during the syntactic analysis]" + Colors.ENDC + "\n")

    else:
        print(Colors.OKGREEN + "[Correct syntactic analysis]" + Colors.ENDC)

    print("=== [File", filename, "verifications is done!] ===")

    return tree, tab_errors
