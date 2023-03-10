import unittest
import main

""" Unit tests class"""
class TestLexer(unittest.TestCase):

    #TODO add more unit tests to test all cases

    #['TURN',
    # 'TURNAFTERCOMMENT',
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
        main.lexer.input('[Nzscf5qWgtgNVX "56BnnQIeAhy"]')
        token = main.lexer.token()

        self.assertEqual(token.type, "COMMENT")
        self.assertEqual(token.value, '[Nzscf5qWgtgNVX "56BnnQIeAhy"]')

    def testComment2(self):
        main.lexer.input('[test "crazy"]')
        token = main.lexer.token()

        self.assertEqual(token.type, "COMMENT")
        self.assertEqual(token.value, '[Nzscf5qWgtgNVX "56BnnQIeAhy"]')

    def testMove1(self):
        main.lexer.input("e4")
        token = main.lexer.token()

        self.assertEqual(token.type, "MOVE")
        self.assertEqual(token.value, "e4")


# Launch all test units
if __name__ == '__main__':
    unittest.main()