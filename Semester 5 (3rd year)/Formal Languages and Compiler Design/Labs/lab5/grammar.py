class Grammar:
    def __init__(self):
        self.nonterminals = []
        self.terminals = []
        self.productions = {}
        self.start_symbol = None

    def read_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return

        # Set nonterminals and terminals
        self.nonterminals = lines[0].strip().split()
        self.terminals = lines[1].strip().split()

        # Set start symbol
        self.start_symbol = lines[2].strip()

        # Read productions
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
        print("Nonterminals:", self.nonterminals)

    def print_terminals(self):
        print("Terminals:", self.terminals)

    def print_productions(self):
        for nonterminal, production_rules in self.productions.items():
            for rule in production_rules:
                print(f"{nonterminal} -> {rule}")

    def first(self):
        first_sets = {nonterminal: set() for nonterminal in self.nonterminals}

        def compute_first(symbol):
            if symbol in self.terminals:
                return {symbol}

            if symbol in first_sets and first_sets[symbol]:
                return first_sets[symbol]

            first_set = set()

            for production in self.productions[symbol]:
                for prod_symbol in production.split():
                    symbol_first = compute_first(prod_symbol)
                    first_set.update(symbol_first - {''})
                    if '' not in symbol_first:
                        break
                else:
                    first_set.add('')

            first_sets[symbol] = first_set
            return first_set

        for nonterminal in self.nonterminals:
            compute_first(nonterminal)

        print("\nFirst Sets:")
        for nonterminal, first_set in first_sets.items():
            print(f"First({nonterminal}) = {first_set}")

        return first_sets

    def follow(self):
        # Initialize follow sets: Each nonterminal gets an empty set initially.
        follow_sets = {nonterminal: set() for nonterminal in self.nonterminals}

        # The start symbol has $ in its follow set, indicating the end of input.
        follow_sets[self.start_symbol].add('$')

        # First, calculate the First sets
        first_sets = self.first()

        # Helper function to compute Follow for a nonterminal
        def compute_follow(symbol):
            # Return if the symbol is a terminal (no follow for terminals)
            if symbol in self.terminals:
                return set()

            # If the follow set for the symbol has been computed before, return it
            if follow_sets[symbol]:
                return follow_sets[symbol]

            follow_set = set()

            # Go through all the production rules
            for left, rights in self.productions.items():
                for right in rights:
                    # If the right side contains the symbol
                    if symbol in right.split():
                        # Find the position of the symbol in the production
                        index = right.split().index(symbol)

                        # Case 1: If the symbol is not the last one in the production
                        if index + 1 < len(right.split()):
                            next_symbol = right.split()[index + 1]
                            # Add First(next_symbol) to Follow(symbol), but without '' (empty string)
                            follow_set.update(first_sets.get(next_symbol, set()) - {''})
                        # Case 2: If the symbol is the last one, or epsilon is in First(next_symbol)
                        elif symbol != left:
                            follow_set.update(compute_follow(left))

            follow_sets[symbol] = follow_set
            return follow_set

        # Compute Follow for all nonterminals
        for nonterminal in self.nonterminals:
            compute_follow(nonterminal)

        # Print the Follow sets
        print("\nFollow Sets:")
        for nonterminal, follow_set in follow_sets.items():
            print(f"Follow({nonterminal}) = {follow_set}")

        return follow_sets

    def print_productions_for_nonterminal(self, nonterminal):
        if nonterminal in self.productions:
            print(f"Productions for {nonterminal}:")
            for production in self.productions[nonterminal]:
                print(f"{nonterminal} -> {production}")
        else:
            print(f"No productions found for nonterminal: {nonterminal}")

    def is_cfg(self):
        # Check if the start symbol is defined and is a valid nonterminal
        if not self.start_symbol or self.start_symbol not in self.nonterminals:
            print("Invalid or undefined start symbol.")
            return False

        # Check for overlap between terminals and nonterminals
        if set(self.terminals).intersection(self.nonterminals):
            print("Overlap found between terminals and nonterminals.")
            return False

        # Check each production rule
        for left, rights in self.productions.items():
            # Left side should be a single nonterminal
            if not (left in self.nonterminals and len(left.split()) == 1):
                print(f"Invalid production rule: {left} -> {rights}")
                return False

            for right in rights:
                if right == '':  # Allowing e-productions
                    continue

                # Split the right part and check each symbol
                for symbol in right.split():
                    if not (symbol in self.terminals or symbol in self.nonterminals):
                        print(f"Unrecognized symbol in production: {left} -> {right}")
                        return False
        return True

    def display_menu(self):
        print("Grammar Operations Menu:")
        print("1. Print Nonterminals")
        print("2. Print Terminals")
        print("3. Print All Productions")
        print("4. Print Productions for a Nonterminal")
        print("5. Check if CFG")
        print("6. Compute First Sets")
        print("7. Compute Follow Sets")  # Added option for Follow sets
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            self.print_nonterminals()
        elif choice == '2':
            self.print_terminals()
        elif choice == '3':
            self.print_productions()
        elif choice == '4':
            nonterminal = input("Enter the nonterminal: ")
            self.print_productions_for_nonterminal(nonterminal)
        elif choice == '5':
            print("Is CFG:", self.is_cfg())
        elif choice == '6':
            self.first()
        elif choice == '7':  # Added this to handle the Follow sets computation
            self.follow()  # Call the follow function to compute Follow sets
        elif choice == '0':
            return
        else:
            print("Invalid choice.")

        # To continue displaying the menu
        input("Press Enter to continue...")
        self.display_menu()


# Example usage:
grammar = Grammar()
grammar.read_from_file('g1.txt')
grammar.display_menu()
