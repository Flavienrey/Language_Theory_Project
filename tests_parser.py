import unittest
from ply import yacc
import chessparser
from chessparser import *

tokens = ['TURN_NUMBER_WITH_DOT', 'TURN_AFTER_COMMENT', 'PIECE', 'MOVE', 'RESULT', 'COMMENT', 'CHECK', 'CHECKMATE',
                       'DESCRIPTION', 'GRADE', 'CASTLING']
""" Unit tests class"""

class TestParser(unittest.TestCase):
    #TODO: TU
    #Game               : OK
    #EventDescriptor    : OK
    #Turn               : NOT OK
    #WhiteMove          : NOT OK
    #BlackMove          : NOT OK
    #WhiteComment       : NOT OK ==> pas la peine ?????
    #BlackComment       : NOT OK ==> pas la peine ?????

    #_______________Tests production Game_______________
    def testGame1_Passant(self):
        parser = yacc.yacc(debug=True)
        input = "[bob \"foo\"] 1. d5 e1 1-0"
        result = chessparser.test(parser,input,"Tests unitaires parser")
        print("result ")
        self.assertEqual(result.children.type, "game")
        self.assertEqual(result.children.value.children[0].type, "eventDescriptor")
        self.assertIsNotNone(result.children.value.children[0].value.children[0].value)
        self.assertEqual(result.children.value.children[1].type, "turn")
        self.assertIsNotNone(result.children.value.children[1].value.children[0].value)
        self.assertEqual(result.children.value.children[2].type, "RESULT")
        self.assertIsNotNone(result.children.value.children[2].value)
        self.assertEqual(result.children.value.children[3].type, "game")
        self.assertIsNone(result.children.value.children[3].value.children[0].value)

    def testGame2_Passant(self):
        parser = yacc.yacc(debug=True)
        input = "[bob \"foo\"] 1. d5 e1 2. a3 b7 1-0 1. d5 e1 2. a3 b7 1/2-1/2"
        result = chessparser.test(parser,input,"Tests unitaires parser")
        print("result ")
        self.assertEqual(result.children.type, "game")
        self.assertEqual(result.children.value.children[0].type, "eventDescriptor")
        self.assertIsNotNone(result.children.value.children[0].value.children[0].value)
        self.assertEqual(result.children.value.children[1].type, "turn")
        self.assertIsNotNone(result.children.value.children[1].value.children[0].value)
        self.assertEqual(result.children.value.children[2].type, "RESULT")
        self.assertIsNotNone(result.children.value.children[2].value)
        self.assertEqual(result.children.value.children[3].type, "game")
        self.assertIsNotNone(result.children.value.children[3].value.children[0].value)

    def testGame3_NonPassant(self):
        parser = yacc.yacc(debug=True)
        input = "[bob \"foo\"] 1. d5 e1 a2 1-0"
        result = chessparser.test(parser,input,"Tests unitaires parser")
        print("result ")
        self.assertEqual(result.children.type, "game")
        self.assertEqual(result.children.value.children[0].type, "eventDescriptor")
        self.assertIsNone(result.children.value.children[0].value.children[0].value)
            #if a symbol terminal is not valid, all symbol terminals are not valid
        self.assertEqual(result.children.value.children[1].type, "turn")
        self.assertIsNone(result.children.value.children[1].value.children[0].value)
        self.assertEqual(result.children.value.children[2].type, "RESULT")
        self.assertIsNotNone(result.children.value.children[2].value)
        self.assertEqual(result.children.value.children[3].type, "game")
        self.assertIsNone(result.children.value.children[3].value.children[0].value)

    #_______________Tests production EventDescriptor_______________
    def testEventDescriptor1_Passant(self):
        parser = yacc.yacc(debug=True)
        input = "[bob \"foo\"] 1. d5 e1 2. b4 e3 1-0"
        result = chessparser.test(parser,input,"Tests unitaires parser")
        print("result ")
        self.assertEqual(result.children.value.children[0].type, "eventDescriptor")
        self.assertEqual(result.children.value.children[0].value.children[0].value, "[bob \"foo\"]")

    def testEventDescriptor2_NonPassant(self):
        parser = yacc.yacc(debug=True)
        input = "[bob foo\"] 1. d5 e1 2. b4 e3 1-0"
        result = chessparser.test(parser,input,"Tests unitaires parser")
        print("result ")
        self.assertEqual(result.children.value.children[0].type, "eventDescriptor")
        self.assertIsNone(result.children.value.children[0].value.children[0].value)

    def testEventDescriptor3_NonPassant(self):
        parser = yacc.yacc(debug=True)
        input = "1. d5 e1 2. b4 e3 1-0"
        result = chessparser.test(parser,input,"Tests unitaires parser")
        print("result ")
        self.assertEqual(result.children.value.children[0].type, "eventDescriptor")
        self.assertIsNone(result.children.value.children[0].value.children[0].value)

    #_______________Tests production Turn_______________
    def testTurn1_Passant(self):
        wait = 1

    def testTurn2_NonPassant(self):
        wait = 1


    #_______________Tests production WhiteMove_______________
    def testWhiteMove1_Passant(self):
        wait = 1

    def testWhiteMove2_NonPassant(self):
        wait = 1

    #_______________Tests production BlackMove_______________
    def testBlackMove1_Passant(self):
        wait = 1

    def testBlackMove2_NonPassant(self):
        wait = 1


    #_______________Tests production WhiteComment_______________
    def testWhiteComment1_Passant(self):
        wait = 1

    def testWhiteComment2_NonPassant(self):
        wait = 1

    #_______________Tests production BlackComment_______________
    def testBlackComment1_Passant(self):
        wait = 1

    def testBlackComment2_NonPassant(self):
        wait = 1
