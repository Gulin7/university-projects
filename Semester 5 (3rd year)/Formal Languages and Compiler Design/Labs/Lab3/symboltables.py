from hashtable import HashTable


class SymbolTableConstants:
    """ Symbol table for constants

    Attributes:
        symboltable (HashTable): HashTable for constants
    """

    def __init__(self):
        self.symboltable = HashTable()

    def addConstantToTable(self, identifier, value):
        self.symboltable.insert(identifier, value)

    def get_constant(self, identifier):
        return self.symboltable.get(identifier)

    def getPosition(self, identifier):
        return self.symboltable.get_position(identifier)


class SymbolTableIdentifiers:
    """ Symbol table for identifiers

    Attributes:
        symboltable (HashTable): HashTable for identifiers
    """

    def __init__(self):
        self.symboltable = HashTable()

    def addIdentifier(self, identifier, value):
        self.symboltable.insert(identifier, value)

    def getIdentifierValue(self, identifier):
        return self.symboltable.get(identifier)

    def getPosition(self, identifier):
        return self.symboltable.get_position(identifier)