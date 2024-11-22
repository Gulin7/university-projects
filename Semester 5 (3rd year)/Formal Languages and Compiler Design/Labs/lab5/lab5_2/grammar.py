class Grammar:
    def __init__(self):
        self.nonterminals = []
        self.terminals = []
        self.productions = {}
        self.start_symbol = None

    def read_from_file(self, file_path):
        """Reads grammar data from a file and populates the grammar."""
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return

        # Extract nonterminals, terminals, and start symbol
        self._parse_nonterminals_and_terminals(lines)
        self._parse_start_symbol(lines)
        self._parse_productions(lines)

    def _parse_nonterminals_and_terminals(self, lines):
        """Helper method to parse nonterminals and terminals."""
        self.nonterminals = lines[0].strip().split()
        self.terminals = lines[1].strip().split()

    def _parse_start_symbol(self, lines):
        """Helper method to parse the start symbol."""
        self.start_symbol = lines[2].strip()

    def _parse_productions(self, lines):
        """Helper method to parse production rules."""
        for line in lines[3:]:
            parts = line.strip().split('->')
            if len(parts) != 2:
                continue  # Skip invalid lines

            left, right = parts
            left = left.strip()

            if left not in self.productions:
                self.productions[left] = []

            right_symbols = [symbol.strip() for symbol in right.split('|')]
            self.productions[left].extend(right_symbols)

    def print_nonterminals(self):
        """Prints all nonterminals."""
        print("Nonterminals:", self.nonterminals)

    def print_terminals(self):
        """Prints all terminals."""
        print("Terminals:", self.terminals)

    def print_productions(self):
        """Prints all production rules."""
        for nonterminal, production_rules in self.productions.items():
            for rule in production_rules:
                print(f"{nonterminal} -> {rule}")

    def print_productions_for_nonterminal(self, nonterminal):
        """Prints the production rules for a specific nonterminal."""
        if nonterminal in self.productions:
            print(f"Productions for {nonterminal}:")
            for production in self.productions[nonterminal]:
                print(f"{nonterminal} -> {production}")
        else:
            print(f"No productions found for nonterminal: {nonterminal}")

    def is_cfg(self):
        """Checks if the grammar is a Context-Free Grammar (CFG)."""
        if not self.start_symbol or self.start_symbol not in self.nonterminals:
            print("Invalid or undefined start symbol.")
            return False

        if set(self.terminals).intersection(self.nonterminals):
            print("Overlap found between terminals and nonterminals.")
            return False

        for left, rights in self.productions.items():
            if not self._is_valid_production_left_side(left):
                print(f"Invalid production rule: {left} -> {rights}")
                return False

            if not self._are_valid_production_right_sides(left, rights):
                return False

        return True

    def _is_valid_production_left_side(self, left):
        """Checks if the left side of a production is a valid nonterminal."""
        return left in self.nonterminals and len(left.split()) == 1

    def _are_valid_production_right_sides(self, left, rights):
        """Checks if the right sides of the production are valid."""
        for right in rights:
            if right == '':  # Allowing e-productions (empty string)
                continue

            for symbol in right.split():
                if not (symbol in self.terminals or symbol in self.nonterminals):
                    print(f"Unrecognized symbol in production: {left} -> {right}")
                    return False
        return True

    def display_menu(self):
        """Displays the menu for grammar operations."""
        menu_options = {
            '1': self.print_nonterminals,
            '2': self.print_terminals,
            '3': self.print_productions,
            '4': self._handle_productions_for_nonterminal,
            '5': self._check_if_cfg,
            '0': self._exit
        }

        while True:
            print("Grammar Operations Menu:")
            print("1. Print Nonterminals")
            print("2. Print Terminals")
            print("3. Print All Productions")
            print("4. Print Productions for a Nonterminal")
            print("5. Check if CFG")
            print("0. Exit")

            choice = input("Enter your choice: ").strip()

            if choice in menu_options:
                menu_options[choice]()
            else:
                print("Invalid choice. Please try again.")

    def _handle_productions_for_nonterminal(self):
        """Handles the option for printing productions for a nonterminal."""
        nonterminal = input("Enter the nonterminal: ").strip()
        self.print_productions_for_nonterminal(nonterminal)

    def _check_if_cfg(self):
        """Handles the option for checking if the grammar is CFG."""
        print("Is CFG:", self.is_cfg())

    def _exit(self):
        """Exits the menu."""
        print("Exiting...")
        exit()

# Example usage:
grammar = Grammar()
grammar.read_from_file('g1.txt')
grammar.display_menu()
