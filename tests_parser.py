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
    #WhiteComment       : NOT OK
    #BlackComment       : NOT OK

    #_______________Tests production Game_______________
    def testGame1_Passant(self):
        parser = ChessParser()

    def testGame2_NonPassant(self):
        parser = ChessParser()
