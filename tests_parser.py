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
    #Turn               : NOT OK => correction pour le comptage des tours
    #WhiteAndBlackMove  : NOT OK => TEXT détecté
    #WhiteComment       : NOT OK => regex à revoir
    #SimpleComment      : NOT OK => regex à revoir

    #_______________Tests production Game_______________
    def testGame1_OK(self):
        input = "[bob \"foo\"] 1. d5 e1 1-0"
        result, tab_errors  = chessparser.test(input,"Unit tests parser")
        print("result ")
        self.assertEqual(result.children.type, "game")
        self.assertEqual(result.children.value.children[0].type, "eventDescriptor")
        self.assertIsNotNone(result.children.value.children[0].value.children[0].value)
        self.assertEqual(result.children.value.children[1].type, "turn")
        self.assertIsNotNone(result.children.value.children[1].value.children[0].value)
        self.assertEqual(result.children.value.children[2].type, "RESULT")
        self.assertIsNotNone(result.children.value.children[2].value)
        self.assertEqual(result.children.value.children[3].type, "game")
        self.assertEqual(len(tab_errors),0)

    def testGame2_OK(self):
        input = "[bob \"foo\"] 1. d5 e1 2. a3 b7 1-0 1. d5 e1 2. a3 b7 1/2-1/2"
        result, tab_errors  = chessparser.test(input,"Unit tests parser")
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
        self.assertEqual(len(tab_errors),0)

    def testGame3_KO(self):
        input = "[bob \"foo\"] 1. d5 e1 a2 1-0"
        result, tab_errors = chessparser.test(input,"Unit tests parser")
        print("result ")
        self.assertEqual(result.children.type, "game")
        self.assertEqual(result.children.value.children[0].type, "eventDescriptor")
        self.assertEqual(result.children.value.children[1].type, "turn")
        self.assertEqual(result.children.value.children[2].type, "RESULT")
        self.assertIsNotNone(result.children.value.children[2].value)
        self.assertEqual(result.children.value.children[3].type, "game")
        self.assertIsNone(result.children.value.children[3].value.children[0].value)
        self.assertIsNot(tab_errors[0].find("MOVE"),-1)
        self.assertIsNot(tab_errors[0].find("a2"),-1)

    #_______________Tests production EventDescriptor_______________
    def testEventDescriptor1_OK(self):
        input = "[bob \"foo\"] 1. d5 e1 2. b4 e3 1-0"
        result, tab_errors  = chessparser.test(input,"Unit tests parser")
        print("result ")
        self.assertEqual(result.children.value.children[0].type, "eventDescriptor")
        self.assertEqual(result.children.value.children[0].value.children[0].value, "[bob \"foo\"]")
        self.assertEqual(len(tab_errors),0)

    def testEventDescriptor2_KO(self):
        input = "1. [bob \"foo\"] d5 e1 2. b4 e3 1-0"
        result, tab_errors = chessparser.test(input,"Unit tests parser")
        print("result ")
        self.assertEqual(result.children.value.children[0].type, "eventDescriptor")
        self.assertIsNone(result.children.value.children[0].value.children[0].value)
        self.assertIsNot(tab_errors[0].find("DESCRIPTION"),-1)
        self.assertIsNot(tab_errors[0].find("[bob \"foo\"]"),-1)

    #_______________Tests production Turn_______________
    def testTurn1_OK(self):
        input = "1. d5 e1 2. b4 e3 3. b1 c6 1-0"
        result, tab_errors  = chessparser.test(input,"Unit tests parser")
        print("result ")
        self.assertEqual(result.children.value.children[1].type, "turn")
        self.assertIsNotNone(result.children.value.children[1].value.children[7].value)
        self.assertIsNotNone(result.children.value.children[1].value.children[7].value.children[7].value)
        self.assertEqual(result.children.value.children[1].value.children[7].value.children[7].value.children[0].value, "3.")
        self.assertEqual(len(tab_errors),0)

    def testTurn2_KO(self): #TODO: A REVOIR
        input = "1. d5 e1 2. b4 e3 4. b1 c6 1-0"
        result, tab_errors = chessparser.test(input,"Unit tests parser")
        print("result ")
        self.assertEqual(result.children.value.children[1].type, "turn")
        self.assertIsNone(result.children.value.children[1].value)
        self.assertIsNot(tab_errors[0].find("TURN"),-1)
        self.assertIsNot(tab_errors[0].find("4."),1)

    #_______________Tests production WhiteAnBlackMove_______________
    def testWhiteAndBlackMove1_OK(self):
        input = "1. d5 Pe1 1-0"
        result, tab_errors  = chessparser.test(input,"Unit tests parser")
        print("result ")
        self.assertEqual(result.children.value.children[1].type, "turn")
        self.assertEqual(result.children.value.children[1].value.children[1].value.children[0].type, "eventPiece")
        self.assertIsNotNone(result.children.value.children[1].value.children[1].value.children[0].value)
        self.assertEqual(result.children.value.children[1].value.children[1].value.children[1].type, "MOVE")
        self.assertIsNotNone(result.children.value.children[1].value.children[1].value.children[1].value)
        self.assertEqual(result.children.value.children[1].value.children[1].value.children[2].type, "eventCheck")
        self.assertIsNotNone(result.children.value.children[1].value.children[1].value.children[2].value)
        self.assertEqual(result.children.value.children[1].value.children[4].value.children[0].type, "eventPiece")
        self.assertIsNotNone(result.children.value.children[1].value.children[4].value.children[0].value)
        self.assertEqual(result.children.value.children[1].value.children[4].value.children[1].type, "MOVE")
        self.assertIsNotNone(result.children.value.children[1].value.children[4].value.children[1].value)
        self.assertEqual(result.children.value.children[1].value.children[4].value.children[2].type, "eventCheck")
        self.assertIsNotNone(result.children.value.children[1].value.children[4].value.children[2].value)
        self.assertEqual(len(tab_errors),0)

    def testWhiteAndBlackMove2_KO(self): #TODO: A REVOIR
        input = "1. d5 eP1 1-0"
        result, tab_errors  = chessparser.test(input,"Unit tests parser")
        print("result ")
        self.assertEqual(result.children.value.children[1].type, "turn")
        self.assertEqual(result.children.value.children[1].value.children[1].value.children[0].type, "eventPiece")
        self.assertIsNotNone(result.children.value.children[1].value.children[1].value.children[0].value)
        self.assertEqual(result.children.value.children[1].value.children[1].value.children[1].type, "MOVE")
        self.assertIsNotNone(result.children.value.children[1].value.children[1].value.children[1].value)
        self.assertEqual(result.children.value.children[1].value.children[1].value.children[2].type, "eventCheck")
        self.assertIsNotNone(result.children.value.children[1].value.children[1].value.children[2].value)
        self.assertIsNone(result.children.value.children[1].value.children[4].value.children[0].value)
        self.assertIsNot(tab_errors[0].find("MOVE"),-1)
        self.assertIsNot(tab_errors[0].find("eP1"),-1)


    #_______________Tests production WhiteComment_______________
    def testWhiteComment1_OK(self): #TODO: Les caratères spéciaux ne passent pas
        input = "1. d5 {er. !f 10%e ff} 1... Pe1 1-0"
        result, tab_errors  = chessparser.test(input,"Unit tests parser")
        print("result ")
        self.assertEqual(result.children.value.children[1].value.children[3].value.children[0].type, "openningCharacter")
        self.assertIsNotNone(result.children.value.children[1].value.children[3].value.children[0].value)
        self.assertEqual(result.children.value.children[1].value.children[3].value.children[1].type, "eventData")
        self.assertIsNotNone(result.children.value.children[1].value.children[3].value.children[1].value)
        self.assertEqual(result.children.value.children[1].value.children[3].value.children[2].type, "simpleComment")
        self.assertIsNone(result.children.value.children[1].value.children[3].value.children[2].value)
        self.assertEqual(result.children.value.children[1].value.children[3].value.children[3].type, "eventData")
        self.assertIsNone(result.children.value.children[1].value.children[3].value.children[3].value)
        self.assertEqual(result.children.value.children[1].value.children[3].value.children[4].type, "closingCharacter")
        self.assertIsNotNone(result.children.value.children[1].value.children[3].value.children[4].value)
        self.assertEqual(result.children.value.children[1].value.children[3].value.children[5].type, "TURN_AFTER_COMMENT")
        self.assertIsNotNone(result.children.value.children[1].value.children[3].value.children[5].value)
        self.assertEqual(len(tab_errors[0]))

    def testWhiteComment2_KO(self):
        input = "1. d5 (er. !f 10%e ff} 1... Qa1 1-0"
        result, tab_errors  = chessparser.test(input,"Unit tests parser")
        print("result ")
        self.assertEqual(result.children.value.children[1].value.children[6].value.children[0].type, "openningCharacter")
        self.assertIsNotNone(result.children.value.children[1].value.children[6].value.children[0].value)
        self.assertEqual(result.children.value.children[1].value.children[6].value.children[1].type, "eventData")
        self.assertIsNotNone(result.children.value.children[1].value.children[6].value.children[1].value)
        self.assertEqual(result.children.value.children[1].value.children[6].value.children[2].type, "simpleComment")
        self.assertIsNone(result.children.value.children[1].value.children[6].value.children[2].value)
        self.assertEqual(result.children.value.children[1].value.children[6].value.children[3].type, "eventData")
        self.assertIsNone(result.children.value.children[1].value.children[6].value.children[3].value)
        self.assertEqual(result.children.value.children[1].value.children[6].value.children[4].type, "closingCharacter")
        self.assertIsNotNone(result.children.value.children[1].value.children[6].value.children[4].value)
        self.assertEqual(result.children.value.children[1].value.children[6].value.children[5].type, "TURN_AFTER_COMMENT")
        self.assertIsNotNone(result.children.value.children[1].value.children[6].value.children[5].value)
        self.assertIsNot(tab_errors[0].find(),-1)

    #_______________Tests production SimpleComment_______________
    def testSimpleComment1_OK(self):
        input = "1. d5 Pe1 {(0-f it's) ff.} 1-0"
        result, tab_errors  = chessparser.test(input,"Unit tests parser")
        print("result ")
        self.assertEqual(result.children.value.children[1].value.children[6].value.children[0].type, "openningCharacter")
        self.assertIsNotNone(result.children.value.children[1].value.children[6].value.children[0].value)
        self.assertEqual(result.children.value.children[1].value.children[6].value.children[1].type, "eventData")
        self.assertIsNotNone(result.children.value.children[1].value.children[6].value.children[1].value)
        self.assertEqual(result.children.value.children[1].value.children[6].value.children[2].type, "simpleComment")
        self.assertIsNone(result.children.value.children[1].value.children[6].value.children[2].value)
        self.assertEqual(result.children.value.children[1].value.children[6].value.children[3].type, "eventData")
        self.assertIsNone(result.children.value.children[1].value.children[6].value.children[3].value)
        self.assertEqual(result.children.value.children[1].value.children[6].value.children[4].type, "closingCharacter")
        self.assertIsNotNone(result.children.value.children[1].value.children[6].value.children[4].value)
        self.assertEqual(result.children.value.children[1].value.children[6].value.children[5].type, "TURN_AFTER_COMMENT")
        self.assertIsNotNone(result.children.value.children[1].value.children[6].value.children[5].value)
        self.assertEqual(len(tab_errors[0]))

    def testSimpleComment2_KO(self):
        input = "1. d5 Pe1 {0-f it's ff.) 1-0"
        result, tab_errors  = chessparser.test(input,"Unit tests parser")
        print("result ")
        self.assertEqual(result.children.value.children[1].value.children[6].value.children[0].type, "openningCharacter")
        self.assertIsNotNone(result.children.value.children[1].value.children[6].value.children[0].value)
        self.assertEqual(result.children.value.children[1].value.children[6].value.children[1].type, "eventData")
        self.assertIsNotNone(result.children.value.children[1].value.children[6].value.children[1].value)
        self.assertEqual(result.children.value.children[1].value.children[6].value.children[2].type, "simpleComment")
        self.assertIsNone(result.children.value.children[1].value.children[6].value.children[2].value)
        self.assertEqual(result.children.value.children[1].value.children[6].value.children[3].type, "eventData")
        self.assertIsNone(result.children.value.children[1].value.children[6].value.children[3].value)
        self.assertEqual(result.children.value.children[1].value.children[6].value.children[4].type, "closingCharacter")
        self.assertIsNotNone(result.children.value.children[1].value.children[6].value.children[4].value)
        self.assertEqual(result.children.value.children[1].value.children[6].value.children[5].type, "TURN_AFTER_COMMENT")
        self.assertIsNotNone(result.children.value.children[1].value.children[6].value.children[5].value)
        self.assertIsNot(tab_errors[0].find(),-1)
