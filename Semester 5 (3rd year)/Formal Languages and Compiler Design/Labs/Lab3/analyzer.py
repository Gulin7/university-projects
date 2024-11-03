from enum import Enum
import re
from symboltables import SymbolTableConstants, SymbolTableIdentifiers


class TokenTypes(Enum):
    """ Enum for defining the token types
    """
    IDENTIFIER = 0
    CONSTANT = 1
    OPERATOR = 2
    RESERVED_WORD = 3
    SEPARATOR = 4


class Analyzer():
    """ class Analyzer for implementing the scanning algorithm

    Methods:
        __init__:
            - initializes the analyzer with the source code file and token file paths.
        - scan_file:
            - analyzes the source code, generates PIF, and manages symbol tables
        - get_tokens:
            - parses the token definitions from the token file and populates dictionaries for reserved words, operators, and separators
        - is_identifier(string):
            - checks if a string is a valid identifier
        - is_constant(string):
            - checks if a string is a valid constant
    """

    def __init__(self, filename, token_file):
        self.filename = filename
        self.token_file = token_file
        self.tableOfConstants = SymbolTableConstants()
        self.indetifiersTable = SymbolTableIdentifiers()
        self.pif = []
        self.reservedWords = {}
        self.operators = {}
        self.separators = {}
        self.get_tokens()
        self.numberOfConstants = 0

    def analyzeFile(self):
        with open(self.filename, 'r') as program:
            numberOfLines = 0
            for line in program:
                numberOfLines += 1
                line = line.rstrip('\n')
                operatorsAndSeparators = r'(;|==|=|!=|\+=|-=|\*=|\/=|<=|>=|[\+\-\*=\/<>!;\[\]\{\}\(\),;]|\|\||&&)'

                for wordWithOpsAndSeps in re.split(operatorsAndSeparators, line):
                    isValid = False

                    if (wordWithOpsAndSeps.startswith('"') or wordWithOpsAndSeps.startswith(
                            ' "')) and wordWithOpsAndSeps.endswith('"'):
                        isValid = True
                        wordWithOpsAndSeps = wordWithOpsAndSeps.replace(' ', '').replace('"', '')
                        if self.tableOfConstants.getPosition(wordWithOpsAndSeps) is None:
                            self.tableOfConstants.addConstantToTable(wordWithOpsAndSeps, self.numberOfConstants)
                            self.pif.append(
                                (TokenTypes.CONSTANT.value, self.tableOfConstants.getPosition(wordWithOpsAndSeps)))
                            self.numberOfConstants += 1

                    elif (wordWithOpsAndSeps.startswith("'") or wordWithOpsAndSeps.startswith(
                            " '")) and wordWithOpsAndSeps.endswith("'"):
                        isValid = True
                        wordWithOpsAndSeps = wordWithOpsAndSeps.replace(' ', '').replace("'", '')
                        if self.tableOfConstants.getPosition(wordWithOpsAndSeps) is None:
                            self.tableOfConstants.addConstantToTable(wordWithOpsAndSeps, self.numberOfConstants)
                            self.pif.append(
                                (TokenTypes.CONSTANT.value, self.tableOfConstants.getPosition(wordWithOpsAndSeps)))
                            self.numberOfConstants += 1

                    if not isValid:
                        for word in wordWithOpsAndSeps.split():
                            if word == '':
                                continue

                            if word[-1] == ';':
                                print(f'Lexical error at line {numberOfLines}\n')
                                return

                            if word in self.reservedWords.keys():
                                self.pif.append((self.reservedWords.get(word), 0))

                            elif word in self.operators.keys():
                                self.pif.append((self.operators.get(word), 0))

                            elif word in self.separators.keys():
                                self.pif.append((self.separators.get(word), 0))

                            elif self.checkConstant(word):
                                if self.tableOfConstants.getPosition(word) is None:
                                    self.tableOfConstants.addConstantToTable(word, self.numberOfConstants)
                                    self.pif.append((TokenTypes.CONSTANT.value, self.tableOfConstants.getPosition(word)))
                                    self.numberOfConstants += 1

                            elif self.checkIdentifier(word):
                                if self.indetifiersTable.getPosition(word) is None:
                                    self.indetifiersTable.addIdentifier(word, None)
                                self.pif.append(
                                    (TokenTypes.IDENTIFIER.value, self.indetifiersTable.getPosition(word)))

                            else:
                                print(f'Lexical error at line {numberOfLines}\n')
                                return

            print('Lexically correct')

        with open('ST.out', 'w') as output:
            print(str(self.indetifiersTable.symboltable))
            output.write(str(self.indetifiersTable.symboltable))
            print(str(self.tableOfConstants.symboltable))
            output.write(str(self.tableOfConstants.symboltable))

        with open('PIF.out', 'w') as output:
            for key, value in self.pif:
                output.write(f"{key} - {value}\n")

    def get_tokens(self):
        toAddIn = TokenTypes.RESERVED_WORD
        lineNumber = 2
        with open(self.token_file, 'r') as token_file:
            for line in token_file:
                line = line.replace('\n', '')

                if line == '[reserved_words]':
                    continue

                if line == '[operators]':
                    toAddIn = TokenTypes.OPERATOR
                    continue

                if line == '[separators]':
                    toAddIn = TokenTypes.SEPARATOR
                    continue

                if toAddIn == TokenTypes.RESERVED_WORD:
                    self.reservedWords[line] = lineNumber

                if toAddIn == TokenTypes.OPERATOR:
                    self.operators[line] = lineNumber

                if toAddIn == TokenTypes.SEPARATOR:
                    self.separators[line] = lineNumber

                lineNumber += 1

    def checkIdentifier(self, string):
        if string[0] == '0' and len(string) > 1:
            return False
        for char in string:
            if not char.isalnum() and char != '_':
                return False

        return True

    def checkConstant(self, string):
        if string[0] == '0' and len(string) > 1:
            return False

        if string[0] == '0' and len(string) == 1:
            return True

        if string[0] == '-' and len(string) > 1:
            string = string[1:]

        for char in string:
            if not char.isdigit():
                return False

        return True