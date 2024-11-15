import re
from enum import Enum
from symboltables import SymbolTableConstants, SymbolTableIdentifiers
from finiteautomata import FiniteAutomata


class TokenTypes(Enum):
    """Enum for defining the token types."""
    IDENTIFIER = 0
    CONSTANT = 1
    OPERATOR = 2
    RESERVED_WORD = 3
    SEPARATOR = 4


class LexicalAnalyzer:
    """Class for implementing the lexical analyzer (scanner)."""

    def __init__(self, filename, token_file):
        self.filename = filename
        self.token_file = token_file
        self.constant_table = SymbolTableConstants()
        self.identifiers_table = SymbolTableIdentifiers()
        self.pif = []  # Program Internal Form
        self.reserved_words = {}
        self.operators = {}
        self.separators = {}
        self.constants_count = 0
        self.finite_automata = FiniteAutomata('FA.in')

        # Load tokens from the token file
        self._load_tokens()

    def scan_file(self):
        """Scans the source code file, generates PIF and manages symbol tables."""
        with open(self.filename, 'r') as program:
            line_count = 0
            for line in program:
                line_count += 1
                line = line.strip()

                # Split by operators and separators
                words = self._split_words(line)
                for word in words:
                    if word:  # Skip empty words
                        self._process_word(word, line_count)

        # Write the output
        self._write_output()

    def _split_words(self, line):
        """Splits a line of code into words based on operators and separators."""
        operators_and_separators = r'(==|=|!=|\+=|-=|\*=|\/=|<=|>=|[\+\-\*=\/<>!;\[\]\{\}\(\),;]|\|\||&&)'
        return re.split(operators_and_separators, line)

    def _process_word(self, word, line_count):
        """Process each word: reserved word, operator, separator, constant, or identifier."""
        if word in self.reserved_words:
            self.pif.append((self.reserved_words[word], 0))
        elif word in self.operators:
            self.pif.append((self.operators[word], 0))
        elif word in self.separators:
            self.pif.append((self.separators[word], 0))
        elif self._is_constant(word):
            self._process_constant(word)
        elif self._is_identifier(word):
            self._process_identifier(word)
        else:
            print(f"Lexical error at line {line_count}: Invalid token '{word}'")
            exit(1)

    def _process_constant(self, word):
        """Process a constant and add it to the symbol table if new."""
        if self.constant_table.get_position(word) is None:
            self.constant_table.add_constant(word, self.constants_count)
            self.constants_count += 1
        constant_pos = self.constant_table.get_position(self.constants_count - 1)
        self.pif.append((TokenTypes.CONSTANT.value, constant_pos))

    def _process_identifier(self, word):
        """Process an identifier and add it to the symbol table if new."""
        if self.identifiers_table.get_position(word) is None:
            self.identifiers_table.add_identifier(word, None)
        identifier_pos = self.identifiers_table.get_position(word)
        self.pif.append((TokenTypes.IDENTIFIER.value, identifier_pos))

    def _load_tokens(self):
        """Load reserved words, operators, and separators from the token file."""
        current_section = None
        with open(self.token_file, 'r') as file:
            for line_no, line in enumerate(file, start=1):
                line = line.strip()
                if line == '[reserved_words]':
                    current_section = TokenTypes.RESERVED_WORD
                elif line == '[operators]':
                    current_section = TokenTypes.OPERATOR
                elif line == '[separators]':
                    current_section = TokenTypes.SEPARATOR
                elif current_section == TokenTypes.RESERVED_WORD:
                    self.reserved_words[line] = line_no
                elif current_section == TokenTypes.OPERATOR:
                    self.operators[line] = line_no
                elif current_section == TokenTypes.SEPARATOR:
                    self.separators[line] = line_no

    def _write_output(self):
        """Write the symbol tables and PIF to output files."""
        with open('ST.out', 'w') as st_file:
            st_file.write(str(self.identifiers_table.symboltable))
            st_file.write("\n")
            st_file.write(str(self.constant_table.symboltable))

        with open('PIF.out', 'w') as pif_file:
            for key, value in self.pif:
                pif_file.write(f"{key} - {value}\n")

    def _is_identifier(self, word):
        """Check if the word is a valid identifier using the FA."""
        return self.finite_automata.check_word_if_identifier(word)

    def _is_constant(self, word):
        """Check if the word is a valid constant (integer, string, or character)."""
        if self.finite_automata.check_word_if_integer_constant(word):
            return True
        pattern_char = re.compile(r"'[a-zA-Z0-9]'")
        pattern_string = re.compile(r'"[a-zA-Z0-9]*"')
        return bool(pattern_char.match(word) or pattern_string.match(word))
