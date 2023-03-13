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

    def testComment1(self):
        lexer = ChessLexer()

        comment = '[Nzscf5qWgtgNVX "56BnnQIeAhy"]'
        lexer.input(comment)
        token = lexer.token()

        self.assertIsNotNone(token)
        self.assertEqual(token.type, "COMMENT")
        self.assertEqual(token.value, comment)

    def testComment2(self):
        lexer = ChessLexer()

        comment ='[test "crazy"]'
        lexer.input(comment)
        token = lexer.token()

        self.assertIsNotNone(token)
        self.assertEqual(token.type, "COMMENT")
        self.assertEqual(token.value, comment)

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