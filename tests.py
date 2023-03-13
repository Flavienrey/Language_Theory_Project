import unittest
from main import ChessLexer

""" Unit tests class"""
class TestLexer(unittest.TestCase):

    #TODO add more unit tests to test all cases

    #['TURN',
    # 'TURN_AFTER_COMMENT',
    # 'PIECE',
    # 'MOVE',
    # 'RESULT',
    # 'COMMENT',
    # 'CHECK',
    # 'CHECKMATE',
    # 'DESCRIPTION',
    #'GRADE',
    #'CASTLING']

    #Tests token TURN
    def testTurn1_Passant(self):
        lexer = ChessLexer()
        turn = '1.'
        lexer.input(turn)
        token = lexer.token()

        self.assertIsNotNone(token)
        self.assertEqual(token.type, "TURN")
        self.assertEqual(token.value, turn)

    def testTurn2_Passant(self):
        lexer = ChessLexer()
        turn = '322.'
        lexer.input(turn)
        token = lexer.token()

        self.assertIsNotNone(token)
        self.assertEqual(token.type, "TURN")
        self.assertEqual(token.value, turn)

    def testTurn3_NonPassant(self):
        lexer = ChessLexer()
        turnAfter = '0.'
        lexer.input(turnAfter)
        token = lexer.token()

        self.assertIsNone(token)

    #Test token TURN_AFTER_COMMENT
    def testTurnAfter1_Passant(self):
        lexer = ChessLexer()
        turnAfter = '2...'
        lexer.input(turnAfter)
        token = lexer.token()

        self.assertIsNotNone(token)
        self.assertEqual(token.type, "TURN_AFTER_COMMENT")
        self.assertEqual(token.value, turnAfter)

    def testTurnAfter2_NonPassant(self):
        lexer = ChessLexer()
        turn = '0.'
        lexer.input(turn)
        token = lexer.token()

        self.assertIsNone(token)


    def testDescription1(self):
        lexer = ChessLexer()

        description = '[Nzscf5qWgtgNVX "56BnnQIeAhy"]'
        lexer.input(description)
        token = lexer.token()

        self.assertIsNotNone(token)
        self.assertEqual(token.type, "DESCRIPTION")
        self.assertEqual(token.value, description)

    def testDescription2(self):
        lexer = ChessLexer()

        description ='[test "crazy"]'
        lexer.input(description)
        token = lexer.token()

        self.assertIsNotNone(token)
        self.assertEqual(token.type, "DESCRIPTION")
        self.assertEqual(token.value, description)

    def testMove1(self):
        lexer = ChessLexer()

        move = "e4"
        lexer.input(move)
        token = lexer.token()

        self.assertIsNotNone(token)
        self.assertEqual(token.type, "MOVE")
        self.assertEqual(token.value, move)


# Launch all test units
if __name__ == '__main__':
    unittest.main()
