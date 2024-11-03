from hashTable import HashTable

class SymbolTable:
    def __init__(self):
        self.symbolTable = HashTable()
    def add(self, key, value):
        self.symbolTable.insert(key, value)
    def get(self, key):
        return self.symbolTable.get(key)
