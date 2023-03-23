import unittest
from chesslexer import ChessLexer

""" Unit tests class"""

class TestLexer(unittest.TestCase):


    #_______________Tests token TURN_NUMBER_WITH_DOT_______________
    def testTurn1_OK(self):
        lexer = ChessLexer()
        turn = '1.'
        lexer.raw_input(turn)
        token = lexer.token()
        print("in test, token : ", token)

        #self.assertIsNotNone(token)
        #self.assertEqual(token.type, "TURN_NUMBER_WITH_DOT")
        #self.assertEqual(token.value, turn)

    def testTurn2_OK(self):
        lexer = ChessLexer()
        turn = '322.'
        lexer.raw_input(turn)
        token = lexer.token()

        self.assertIsNotNone(token)
        self.assertEqual(token.type, "TURN_NUMBER_WITH_DOT")
        self.assertEqual(token.value, turn)

    def testTurn3_KO(self):
        lexer = ChessLexer()
        turn_after = '0.'
        lexer.raw_input(turn_after)
        token = lexer.token()

        self.assertIsNone(token)

    def testTurn4_KO(self):
       lexer = ChessLexer()
       turn = '-3.'
       lexer.raw_input(turn)
       token = lexer.token()

       self.assertIsNotNone(token)
       self.assertEqual(token.type, "TURN_NUMBER_WITH_DOT")
       self.assertEqual(token.value, '3.')


    #_______________Tests token TURN_AFTER_COMMENT_______________
    def testTurnAfter1_OK(self):
        lexer = ChessLexer()
        turn_after = '2...'
        lexer.raw_input(turn_after)
        token = lexer.token()

        self.assertIsNotNone(token)
        self.assertEqual(token.type, "TURN_AFTER_COMMENT")
        self.assertEqual(token.value, turn_after)

    def testTurnAfter2_KO(self):
        lexer = ChessLexer()
        turn_after = '0...'
        lexer.raw_input(turn_after)
        token = lexer.token()

        self.assertIsNone(token)

    def testTurnAfter3_KO(self):
        lexer = ChessLexer()
        turn_after = '4..'
        lexer.raw_input(turn_after)
        token = lexer.token()

        self.assertIsNotNone(token)
        self.assertIsNot(token.type, "TURN_AFTER_COMMENT")
        self.assertIsNot(token.value, turn_after)


    #_______________Tests token PIECE_______________
    def testPiece1_OK(self):
        lexer = ChessLexer()
        piece = 'P'
        lexer.raw_input(piece)
        token = lexer.token()

        self.assertIsNotNone(token)
        self.assertEqual(token.type, "PIECE")
        self.assertEqual(token.value, piece)

    def testPiece2_KO(self):
        lexer = ChessLexer()
        piece = 'p'
        lexer.raw_input(piece)
        token = lexer.token()

        self.assertIsNot(token.type, "PIECE")

    def testPiece3_KO(self):
        lexer = ChessLexer()
        piece = 'V'
        lexer.raw_input(piece)
        token = lexer.token()

        self.assertIsNot(token.type, "PIECE")


    #_______________Tests token MOVE_______________
    def testMove1_OK(self):
        lexer = ChessLexer()
        move = 'ad3'
        lexer.raw_input(move)
        token = lexer.token()

        self.assertIsNotNone(token)
        self.assertEqual(token.type, "MOVE")
        self.assertEqual(token.value, move)

    def testMove2_KO(self):
        lexer = ChessLexer()
        move = 'xf7'
        lexer.raw_input(move)
        token = lexer.token()

        self.assertIsNotNone(token)
        self.assertEqual(token.type, "MOVE")
        self.assertEqual(token.value, move)

    def testMove3_KO(self):
        lexer = ChessLexer()
        move = 'Ad3'
        lexer.raw_input(move)
        token = lexer.token()

        self.assertIsNot(token.type, "MOVE")

    def testMove4_KO(self):
        lexer = ChessLexer()
        move = 'n4'
        lexer.raw_input(move)
        token = lexer.token()

        self.assertIsNot(token.type, "MOVE")


    #_______________Tests token RESULT_______________
    def testResult1_OK(self):
        lexer = ChessLexer()
        result = '0-1'
        lexer.raw_input(result)
        token = lexer.token()

        self.assertIsNotNone(token)
        self.assertEqual(token.type, "RESULT")
        self.assertEqual(token.value, result)

    def testResult2_OK(self):
        lexer = ChessLexer()
        result = '1/2-1/2'
        lexer.raw_input(result)
        token = lexer.token()

        self.assertIsNotNone(token)
        self.assertEqual(token.type, "RESULT")
        self.assertEqual(token.value, result)

    def testResult3_KO(self):
        lexer = ChessLexer()
        result = '1/ 2-1/2'
        lexer.raw_input(result)
        token = lexer.token()

        self.assertEqual(token.type, "TEXT")

    def testResult4_KO(self):
        lexer = ChessLexer()
        result = '1-1'
        lexer.raw_input(result)
        token = lexer.token()

        self.assertIsNone(token)


    #_______________Tests token CHECK_______________
    def testCheck1_OK(self):
        lexer = ChessLexer()
        check = '+'
        lexer.raw_input(check)
        token = lexer.token()

        self.assertEqual(token.type, "CHECK")
        self.assertEqual(token.value, check)

    def testCheck2_OK(self):
        lexer = ChessLexer()
        check = 'a2+'
        lexer.raw_input(check)

        token = lexer.token()
        token2 = lexer.token()

        self.assertIsNot(token.type, "CHECK")
        self.assertEqual(token.type, "MOVE")
        self.assertEqual(token2.type, "CHECK")

    def testCheck3_KO(self):
        lexer = ChessLexer()
        check = '++'
        lexer.raw_input(check)
        token = lexer.token()

        self.assertIsNot(token.type, "CHECK")


    #_______________Tests token CHECKMATE_______________
    def testCheckmate1_OK(self):
        lexer = ChessLexer()
        checkmate = '++'
        lexer.raw_input(checkmate)
        token = lexer.token()

        self.assertEqual(token.type, "CHECKMATE")
        self.assertEqual(token.value, checkmate)


    def testCheckmate2_OK(self):
        lexer = ChessLexer()
        checkmate = 'b5++'
        lexer.raw_input(checkmate)
        token = lexer.token()
        token2 = lexer.token()

        self.assertIsNot(token.type, "CHECKMATE")
        self.assertEqual(token.type, "MOVE")
        self.assertEqual(token2.type, "CHECKMATE")


    #_______________Tests token DESCRIPTION_______________
    def testDescription1_OK(self):
        lexer = ChessLexer()
        description = '[Nzscf5qWgtgNVX "56BnnQIeAhy"]'
        lexer.raw_input(description)
        token = lexer.token()

        self.assertIsNotNone(token)
        self.assertEqual(token.type, "DESCRIPTION")
        self.assertEqual(token.value, description)

    def testDescription2_OK(self):
        lexer = ChessLexer()
        description ='[test "crazy"]'
        lexer.raw_input(description)
        token = lexer.token()

        self.assertIsNotNone(token)
        self.assertEqual(token.type, "DESCRIPTION")
        self.assertEqual(token.value, description)

    def testDescription3_KO(self):
        lexer = ChessLexer()
        description ='[test@ "crazy"]'
        lexer.raw_input(description)
        token = lexer.token()

        self.assertIsNot(token.type, "DESCRIPTION")

    def testDescription4_OK(self):
        lexer = ChessLexer()
        description ='[test "@crazy!"]'
        lexer.raw_input(description)
        token = lexer.token()

        self.assertIsNotNone(token)
        self.assertEqual(token.type, "DESCRIPTION")
        self.assertEqual(token.value, description)


#_______________Tests token GRADE_______________
    def testGrade1_OK(self):
        lexer = ChessLexer()
        grade = '?'
        lexer.raw_input(grade)
        token = lexer.token()

        self.assertEqual(token.type, "GRADE")
        self.assertEqual(token.value, grade)

    def testGrade2_OK(self):
        lexer = ChessLexer()
        grade = '!'
        lexer.raw_input(grade)
        token = lexer.token()

        self.assertEqual(token.type, "GRADE")
        self.assertEqual(token.value, grade)

    def testGrade3_KO(self):
        lexer = ChessLexer()
        grade = '.'
        lexer.raw_input(grade)
        token = lexer.token()

        self.assertIsNone(token)


#_______________Tests token CASTLING_______________
    def testCastling1_OK(self):
        lexer = ChessLexer()
        castling = 'O-O'
        lexer.raw_input(castling)
        token = lexer.token()

        self.assertEqual(token.type, "CASTLING")
        self.assertEqual(token.value, castling)

    def testCastling2_OK(self):
        lexer = ChessLexer()
        castling = 'O-O-O'
        lexer.raw_input(castling)
        token = lexer.token()

        self.assertEqual(token.type, "CASTLING")
        self.assertEqual(token.value, castling)

    def testCastling3_KO(self):
        lexer = ChessLexer()
        castling = '0-O'
        lexer.raw_input(castling)
        token = lexer.token()

        self.assertIsNot(token.type, "CASTLING")


    #_______________Tests COMMENT (tokens : TEXT, OPENING_PARENTHESIS,CLOSING_PARENTHESIS, OPENING_BRACE, CLOSING_BRACE _______________
    def testComment1_OK(self):
        lexer = ChessLexer()
        comment = '( test xd4)'
        lexer.raw_input(comment)
        token1 = lexer.token()
        token2 = lexer.token()
        token3 = lexer.token()
        token4 = lexer.token()
        print(token1)
        print(token2)
        print(token3)
        print(token4)
        self.assertEqual(token1.type, "OPENING_PARENTHESIS")
        self.assertEqual(token2.type, "TEXT")
        self.assertEqual(token3.type, "MOVE")
        self.assertEqual(token4.type, "CLOSING_PARENTHESIS")

    def testComment2_OK(self):
        lexer = ChessLexer()
        comment = '{ ( bla ) }'
        lexer.raw_input(comment)
        token1 = lexer.token()
        token2 = lexer.token()
        token3 = lexer.token()
        token4 = lexer.token()
        token5 = lexer.token()
        print(token1)
        print(token2)
        print(token3)
        print(token4)
        print(token5)
        self.assertEqual(token1.type, "OPENING_BRACE")
        self.assertEqual(token2.type, "OPENING_PARENTHESIS")
        self.assertEqual(token3.type, "TEXT")
        self.assertEqual(token4.type, "CLOSING_PARENTHESIS")
        self.assertEqual(token5.type, "CLOSING_BRACE")



    #_______________Tests token TEXT_______________

# Launch all test units
if __name__ == '__main__':
    unittest.main()
