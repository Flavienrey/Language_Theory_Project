import unittest
from main import ChessLexer

""" Unit tests class"""
class TestLexer(unittest.TestCase):

    #TODO add more unit tests to test all cases

    #['TURN'                        not OK     ==> en cours  : 1 un TODO à finir : gestion du -
    # 'TURN_AFTER_COMMENT',         OK
    # 'PIECE',                      in progress     ==> 1 un TODO à finir : gestion du -
    # 'MOVE',                       OK
    # 'RESULT',                     in progress     ==> 1 un TODO à finir
    # 'COMMENT',                    not OK
    # 'CHECK',                      not OK
    # 'CHECKMATE',                  not OK
    # 'DESCRIPTION',                in progress     ==> faire cas non passant
    # 'GRADE',                      not OK
    # 'CASTLING']                   not OK

    #_______________Tests token TURN_______________
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
        turn_after = '0.'
        lexer.input(turn_after)
        token = lexer.token()

        self.assertIsNone(token)

    #TODO Cet exemple est reconnu comme Turn, est-ce bien ? doit-on corriger la regex ?
    #def testTurn4_NonPassant(self):
    #    lexer = ChessLexer()
    #    turn_after = '-3.'
    #    lexer.input(turn_after)
    #    token = lexer.token()
    #    print(token)
    #    self.assertIsNone(token)

    #_______________Tests token TURN_AFTER_COMMENT_______________
    def testTurnAfter1_Passant(self):
        lexer = ChessLexer()
        turn_after = '2...'
        lexer.input(turn_after)
        token = lexer.token()

        self.assertIsNotNone(token)
        self.assertEqual(token.type, "TURN_AFTER_COMMENT")
        self.assertEqual(token.value, turn_after)

    def testTurnAfter2_NonPassant(self):
        lexer = ChessLexer()
        turn = '0...'
        lexer.input(turn)
        token = lexer.token()

        self.assertIsNone(token)

    #_______________Tests token PIECE_______________
    def testPiece1_Passant(self):
        lexer = ChessLexer()
        piece = 'P'
        lexer.input(piece)
        token = lexer.token()

        self.assertIsNotNone(token)
        self.assertEqual(token.type, "PIECE")
        self.assertEqual(token.value, piece)

    def testPiece2_NonPassant(self):
        lexer = ChessLexer()
        piece = 'p'
        lexer.input(piece)
        token = lexer.token()

        self.assertIsNone(token)

    def testPiece3_NonPassant(self):
        lexer = ChessLexer()
        piece = 'V'
        lexer.input(piece)
        token = lexer.token()

        self.assertIsNone(token)

    #TODO cet exemple est reconnu comme pièce, est-ce bien ? doit-on corriger la regex ?
    #def testPiece4_NonPassant(self):
    #    lexer = ChessLexer()
    #    piece = '-K'
    #    lexer.input(piece)
    #    token = lexer.token()
    #
    #    self.assertIsNone(token)


    #_______________Tests token MOVE_______________
    def testMove1_Passant(self):
        lexer = ChessLexer()
        move = 'ad3'
        lexer.input(move)
        token = lexer.token()

        self.assertIsNotNone(token)
        self.assertEqual(token.type, "MOVE")
        self.assertEqual(token.value, move)

    def testMove2_Passant(self):
        lexer = ChessLexer()
        move = 'xf7'
        lexer.input(move)
        token = lexer.token()

        self.assertIsNotNone(token)
        self.assertEqual(token.type, "MOVE")
        self.assertEqual(token.value, move)

    def testMove3_NonPassant(self):
        lexer = ChessLexer()
        move = 'Ad3'
        lexer.input(move)
        token = lexer.token()

        self.assertIsNot(token.type, "MOVE")

    def testMove4_NonPassant(self):
        lexer = ChessLexer()
        move = 'n4'
        lexer.input(move)
        token = lexer.token()

        self.assertIsNone(token)


    #_______________Tests token RESULT_______________
    def testResult1_Passant(self):
        lexer = ChessLexer()
        result = '0-1'
        lexer.input(result)
        token = lexer.token()

        self.assertIsNotNone(token)
        self.assertEqual(token.type, "RESULT")
        self.assertEqual(token.value, result)

    def testResult2_Passant(self):
        lexer = ChessLexer()
        result = '1/2-1/2'
        lexer.input(result)
        token = lexer.token()

        self.assertIsNotNone(token)
        self.assertEqual(token.type, "RESULT")
        self.assertEqual(token.value, result)

    def testResult3_NonPassant(self):
        lexer = ChessLexer()
        result = '1/ 2-1/2'
        lexer.input(result)
        token = lexer.token()

        self.assertIsNone(token)

#TODO Vérifier que 1-1 n'apparaisse pas dans une partie, car actuellement toutes les regex le rejette
    #def testResult4_NonPassant(self):
    #    lexer = ChessLexer()
    #    result = '1-1'
    #    lexer.input(result)
    #    token = lexer.token()

    #    self.assertIsNot(token.type, "RESULT")


    #_______________Tests token DESCRIPTION_______________
    def testDescription1_Passant(self):
        lexer = ChessLexer()

        description = '[Nzscf5qWgtgNVX "56BnnQIeAhy"]'
        lexer.input(description)
        token = lexer.token()

        self.assertIsNotNone(token)
        self.assertEqual(token.type, "DESCRIPTION")
        self.assertEqual(token.value, description)

    def testDescription2_Passant(self):
        lexer = ChessLexer()

        description ='[test "crazy"]'
        lexer.input(description)
        token = lexer.token()

        self.assertIsNotNone(token)
        self.assertEqual(token.type, "DESCRIPTION")
        self.assertEqual(token.value, description)


# Launch all test units
if __name__ == '__main__':
    unittest.main()
