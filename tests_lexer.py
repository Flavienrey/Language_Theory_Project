import unittest
from chesslexer import ChessLexer

""" Unit tests class"""

class TestLexer(unittest.TestCase):

    #_______________Tests token TURN_______________
    def testTurn1_Passant(self):
        lexer = ChessLexer()
        turn = '1.'
        lexer.raw_input(turn)
        token = lexer.token()

        self.assertIsNotNone(token)
        self.assertEqual(token.type, "TURN")
        self.assertEqual(token.value, turn)

    def testTurn2_Passant(self):
        lexer = ChessLexer()
        turn = '322.'
        lexer.raw_input(turn)
        token = lexer.token()

        self.assertIsNotNone(token)
        self.assertEqual(token.type, "TURN")
        self.assertEqual(token.value, turn)

    def testTurn3_NonPassant(self):
        lexer = ChessLexer()
        turn_after = '0.'
        lexer.raw_input(turn_after)
        token = lexer.token()

        self.assertIsNone(token)

    def testTurn4_Passant(self):
       lexer = ChessLexer()
       turn = '-3.'
       lexer.raw_input(turn)
       token = lexer.token()

       self.assertIsNotNone(token)
       self.assertEqual(token.type, "TURN")
       self.assertEqual(token.value, '3.')


    #_______________Tests token TURN_AFTER_COMMENT_______________
    def testTurnAfter1_Passant(self):
        lexer = ChessLexer()
        turn_after = '2...'
        lexer.raw_input(turn_after)
        token = lexer.token()

        self.assertIsNotNone(token)
        self.assertEqual(token.type, "TURN_AFTER_COMMENT")
        self.assertEqual(token.value, turn_after)

    def testTurnAfter2_NonPassant(self):
        lexer = ChessLexer()
        turn_after = '0...'
        lexer.raw_input(turn_after)
        token = lexer.token()

        self.assertIsNone(token)

    def testTurnAfter3_NonPassant(self):
        lexer = ChessLexer()
        turn_after = '4..'
        lexer.raw_input(turn_after)
        token = lexer.token()

        self.assertIsNotNone(token)
        self.assertIsNot(token.type, "TURN_AFTER_COMMENT")
        self.assertIsNot(token.value, turn_after)


    #_______________Tests token PIECE_______________
    def testPiece1_Passant(self):
        lexer = ChessLexer()
        piece = 'P'
        lexer.raw_input(piece)
        token = lexer.token()

        self.assertIsNotNone(token)
        self.assertEqual(token.type, "PIECE")
        self.assertEqual(token.value, piece)

    def testPiece2_NonPassant(self):
        lexer = ChessLexer()
        piece = 'p'
        lexer.raw_input(piece)
        token = lexer.token()

        self.assertIsNone(token)

    def testPiece3_NonPassant(self):
        lexer = ChessLexer()
        piece = 'V'
        lexer.raw_input(piece)
        token = lexer.token()

        self.assertIsNone(token)


    #_______________Tests token MOVE_______________
    def testMove1_Passant(self):
        lexer = ChessLexer()
        move = 'ad3'
        lexer.raw_input(move)
        token = lexer.token()

        self.assertIsNotNone(token)
        self.assertEqual(token.type, "MOVE")
        self.assertEqual(token.value, move)

    def testMove2_Passant(self):
        lexer = ChessLexer()
        move = 'xf7'
        lexer.raw_input(move)
        token = lexer.token()

        self.assertIsNotNone(token)
        self.assertEqual(token.type, "MOVE")
        self.assertEqual(token.value, move)

    def testMove3_NonPassant(self):
        lexer = ChessLexer()
        move = 'Ad3'
        lexer.raw_input(move)
        token = lexer.token()

        self.assertIsNot(token.type, "MOVE")

    def testMove4_NonPassant(self):
        lexer = ChessLexer()
        move = 'n4'
        lexer.raw_input(move)
        token = lexer.token()

        self.assertIsNone(token)


    #_______________Tests token RESULT_______________
    def testResult1_Passant(self):
        lexer = ChessLexer()
        result = '0-1'
        lexer.raw_input(result)
        token = lexer.token()

        self.assertIsNotNone(token)
        self.assertEqual(token.type, "RESULT")
        self.assertEqual(token.value, result)

    def testResult2_Passant(self):
        lexer = ChessLexer()
        result = '1/2-1/2'
        lexer.raw_input(result)
        token = lexer.token()

        self.assertIsNotNone(token)
        self.assertEqual(token.type, "RESULT")
        self.assertEqual(token.value, result)

    def testResult3_NonPassant(self):
        lexer = ChessLexer()
        result = '1/ 2-1/2'
        lexer.raw_input(result)
        token = lexer.token()

        self.assertIsNone(token)

    def testResult4_NonPassant(self):
        lexer = ChessLexer()
        result = '1-1'
        lexer.raw_input(result)
        token = lexer.token()

        self.assertIsNone(token)

    #_______________Tests token COMMENT_______________
    def testComment1_Passant(self):
        lexer = ChessLexer()
        comment = '(jflzjesl& 4. ! xd4)'
        lexer.raw_input(comment)
        token = lexer.token()

        self.assertEqual(token.type, "COMMENT")
        self.assertEqual(token.value, comment)

    def testComment2_Passant(self):
        lexer = ChessLexer()
        comment = '{ bla bla (jflzjesl& 4. ! xd4) bla bla}'
        lexer.raw_input(comment)
        token = lexer.token()

        self.assertEqual(token.type, "COMMENT")
        self.assertEqual(token.value, comment)

    def testComment3_NonPassant(self):
        lexer = ChessLexer()
        comment = '{ bla bla )'
        lexer.raw_input(comment)
        token = lexer.token()

        self.assertIsNone(token)

    #_______________Tests token CHECK_______________
    def testCheck1_Passant(self):
        lexer = ChessLexer()
        check = '+'
        lexer.raw_input(check)
        token = lexer.token()

        self.assertEqual(token.type, "CHECK")
        self.assertEqual(token.value, check)

    def testCheck2_Passant(self):
        lexer = ChessLexer()
        check = 'a2+'
        lexer.raw_input(check)

        token = lexer.token()
        token2 = lexer.token()

        self.assertIsNot(token.type, "CHECK")
        self.assertEqual(token.type, "MOVE")
        self.assertEqual(token2.type, "CHECK")

    def testCheck3_NonPassant(self):
        lexer = ChessLexer()
        check = '++'
        lexer.raw_input(check)
        token = lexer.token()

        self.assertIsNot(token.type, "CHECK")


    #_______________Tests token CHECKMATE_______________
    def testCheckmate1_Passant(self):
        lexer = ChessLexer()
        checkmate = '++'
        lexer.raw_input(checkmate)
        token = lexer.token()

        self.assertEqual(token.type, "CHECKMATE")
        self.assertEqual(token.value, checkmate)


    def testCheckmate2_Passant(self):
        lexer = ChessLexer()
        checkmate = 'b5++'
        lexer.raw_input(checkmate)
        token = lexer.token()
        token2 = lexer.token()

        self.assertIsNot(token.type, "CHECKMATE")
        self.assertEqual(token.type, "MOVE")
        self.assertEqual(token2.type, "CHECKMATE")


    #_______________Tests token DESCRIPTION_______________
    def testDescription1_Passant(self):
        lexer = ChessLexer()
        description = '[Nzscf5qWgtgNVX "56BnnQIeAhy"]'
        lexer.raw_input(description)
        token = lexer.token()

        self.assertIsNotNone(token)
        self.assertEqual(token.type, "DESCRIPTION")
        self.assertEqual(token.value, description)

    def testDescription2_Passant(self):
        lexer = ChessLexer()
        description ='[test "crazy"]'
        lexer.raw_input(description)
        token = lexer.token()

        self.assertIsNotNone(token)
        self.assertEqual(token.type, "DESCRIPTION")
        self.assertEqual(token.value, description)

    def testDescription3_NonPassant(self):
        lexer = ChessLexer()
        description ='[test@ "crazy"]'
        lexer.raw_input(description)
        token = lexer.token()

        self.assertIsNone(token)

    def testDescription4_Passant(self):
        lexer = ChessLexer()
        description ='[test "@crazy!"]'
        lexer.raw_input(description)
        token = lexer.token()

        self.assertIsNotNone(token)
        self.assertEqual(token.type, "DESCRIPTION")
        self.assertEqual(token.value, description)


#_______________Tests token GRADE_______________
    def testGrade1_Passant(self):
        lexer = ChessLexer()
        grade = '?'
        lexer.raw_input(grade)
        token = lexer.token()

        self.assertEqual(token.type, "GRADE")
        self.assertEqual(token.value, grade)

    def testGrade2_Passant(self):
        lexer = ChessLexer()
        grade = '!'
        lexer.raw_input(grade)
        token = lexer.token()

        self.assertEqual(token.type, "GRADE")
        self.assertEqual(token.value, grade)

    def testGrade3_NonPassant(self):
        lexer = ChessLexer()
        grade = '.'
        lexer.raw_input(grade)
        token = lexer.token()

        self.assertIsNone(token)


#_______________Tests token CASTLING_______________
    def testCastling1_Passant(self):
        lexer = ChessLexer()
        castling = 'O-O'
        lexer.raw_input(castling)
        token = lexer.token()

        self.assertEqual(token.type, "CASTLING")
        self.assertEqual(token.value, castling)

    def testCastling2_Passant(self):
        lexer = ChessLexer()
        castling = 'O-O-O'
        lexer.raw_input(castling)
        token = lexer.token()

        self.assertEqual(token.type, "CASTLING")
        self.assertEqual(token.value, castling)

    def testCastling3_NonPassant(self):
        lexer = ChessLexer()
        castling = '0-O'
        lexer.raw_input(castling)
        token = lexer.token()

        self.assertIsNone(token)


# Launch all test units
if __name__ == '__main__':
    unittest.main()
