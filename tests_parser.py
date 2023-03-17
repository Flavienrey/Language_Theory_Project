import unittest
from chessparser import ChessParser

""" Unit tests class"""

class TestParser(unittest.TestCase):
    #TODO: TU
    #Game               : NOT OK
    #EventDescriptor    : NOT OK
    #Turn               : NOT OK
    #WhiteMove          : NOT OK
    #BlackMove          : NOT OK
    #EventCheck         : NOT OK
    #EventCheckMate     : NOT OK
    #WhiteComment       : NOT OK
    #BlackComment       : NOT OK

    #_______________Tests production Game_______________
    def testGame1_Passant(self):
        parser = ChessParser()

    def testGame2_NonPassant(self):
        parser = ChessParser()

    #_______________Tests production EventDescriptor_______________
    def testEventDescriptor1_Passant(self):
        parser = ChessParser()

    def testEventDescriptor2_NonPassant(self):
        parser = ChessParser()

    #_______________Tests production Turn_______________
    def testTurn1_Passant(self):
        parser = ChessParser()

    def testTurn2_NonPassant(self):
        parser = ChessParser()

    #_______________Tests production WhiteMove_______________
    def testWhiteMove1_Passant(self):
        parser = ChessParser()

    def testWhiteMove2_NonPassant(self):
        parser = ChessParser()

    #_______________Tests production BlackMove_______________
    def testBlackMove1_Passant(self):
        parser = ChessParser()

    def testBlackMove2_NonPassant(self):
        parser = ChessParser()

    #_______________Tests production EventCheck_______________
    def testEventCheck1_Passant(self):
        parser = ChessParser()

    def testEventCheck2_NonPassant(self):
        parser = ChessParser()

    #_______________Tests production EventCheckMate_______________
    def testEventCheckMate1_Passant(self):
        parser = ChessParser()

    def testEventCheckMate2_NonPassant(self):
        parser = ChessParser()

    #_______________Tests production WhiteComment_______________
    def testWhiteComment1_Passant(self):
        parser = ChessParser()

    def testWhiteComment2_NonPassant(self):
        parser = ChessParser()

    #_______________Tests production BlackComment_______________
    def testBlackComment1_Passant(self):
        parser = ChessParser()

    def testBlackComment2_NonPassant(self):
        parser = ChessParser()
