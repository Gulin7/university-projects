import unittest
from symbolTable import SymbolTable

class TestSymbolTableWithIdentifiers(unittest.TestCase):
    def __init__(self):
        self.identifiers = SymbolTable()

    def runTests(self):
        self.identifiers.add("a", 1)
        assert(self.identifiers.get("a") == 1)
        self.identifiers.add("b", 2)
        assert(self.identifiers.get("b") == 2)
        self.identifiers.add("c", "three")
        assert(self.identifiers.get("c") == "three")
        self.identifiers.add("d", "four")
        assert(self.identifiers.get("d") == "four")
        self.identifiers.add("e", 5)
        assert(self.identifiers.get("e") == 5)
        self.identifiers.add("f", 6)
        assert(self.identifiers.get("f") == 6)
        self.identifiers.add("g", 7)
        assert(self.identifiers.get("g") == 7)