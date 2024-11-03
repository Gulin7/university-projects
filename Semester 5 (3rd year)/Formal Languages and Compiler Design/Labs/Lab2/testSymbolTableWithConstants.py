import unittest
from symbolTable import SymbolTable

class TestSymbolTableWithConstants(unittest.TestCase):
    def __init__(self):
        self.constants = SymbolTable()

    def runTests(self):
        self.constants.add(1, 2)
        assert(self.constants.get(1) == 2)
        self.constants.add(2, 3)
        assert(self.constants.get(2) == 3)
        self.constants.add(3, "four")
        assert(self.constants.get(3) == "four")
        self.constants.add(4, "five")
        assert(self.constants.get(4) == "five")
        self.constants.add(5, 6)
        assert(self.constants.get(5) == 6)
        self.constants.add(6, 7)
        assert(self.constants.get(6) == 7)
