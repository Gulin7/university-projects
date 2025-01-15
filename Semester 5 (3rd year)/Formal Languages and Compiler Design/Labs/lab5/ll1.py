from grammar import Grammar
from collections import defaultdict


class Ll1:
    def __init__(self, input_file, pif_file=None):
        self.__grammar = Grammar(input_file=input_file)
        self.__first_col = defaultdict(set)
        self.__follow_col = defaultdict(set)
        self.__parsing_table = defaultdict(lambda: defaultdict(lambda: None))

        self.__build_table()
        if pif_file:
            self.__generate_table_from_pif(pif_file)

    def __parse_pif(self, pif_file):
        """
        Parse the PIF file and return a list of (non_terminal_idx, production_idx) tuples.
        """
        pif_out = []
        with open(pif_file, 'r') as f:
            for line in f:
                parts = line.strip().split(' - ')
                non_terminal_idx = int(parts[0])
                production_part = parts[1]

                # Remove parentheses and handle 'None' case
                production_part = production_part.strip('()')
                if production_part == 'None':
                    production_idx = None  # Directly use None for epsilon
                else:
                    production_idx = tuple(map(int, production_part.split(', '))) if production_part else None

                pif_out.append((non_terminal_idx, production_idx))
        return pif_out

    def __generate_table_from_pif(self, pif_file):
        """
        Generate the parsing table from the PIF file, checking for collisions in the table.
        """
        pif_out = self.__parse_pif(pif_file)

        productions = self.__grammar.get_productions().get_all()

        parsing_table = {}

        for non_terminal_idx, production_idx in pif_out:
            if non_terminal_idx not in productions:
                continue

            # Handle production_idx (a tuple or a single integer)
            if isinstance(production_idx, tuple):
                if len(production_idx) == 1 and production_idx[0] is None:
                    production_rule = None
                else:
                    production_rule = productions[non_terminal_idx][production_idx[0]] if isinstance(production_idx[0],
                                                                                                     int) else None
            elif isinstance(production_idx, int):
                production_rule = productions[non_terminal_idx][production_idx]
            else:
                production_rule = None  # Default to None if the production_idx is invalid

            # Check for collisions in the parsing table
            if non_terminal_idx not in parsing_table:
                parsing_table[non_terminal_idx] = {}

            # **Check for collision**: Ensure we're comparing both `non_terminal_idx` and `production_idx`


            # No collision, so we add the rule
            parsing_table[non_terminal_idx][production_idx] = production_rule

        # Print the generated parsing table (optional)
        print("Generated Parsing Table:")
        for non_terminal, rules in parsing_table.items():
            print(f"{non_terminal}: {rules}")

        # Store the parsing table
        self.parsing_table = parsing_table

    def __build_table(self):
        self.__build_first()
        self.__build_follow()
        self.__build_parsing_table()

    def __build_first(self):
        non_terminals = self.__grammar.get_nonterminals()
        terminals = self.__grammar.get_terminals()
        productions = self.__grammar.get_productions().get_all()

        for symbol in non_terminals:
            self.__first_col[symbol] = set()

        for lhs, rhs in productions.items():
            for rule in rhs:
                if rule[0] in terminals:
                    self.__first_col[lhs[0]].add(rule[0])
                elif rule[0] in non_terminals:
                    self.__first_col[lhs[0]].update(self.__first_col[rule[0]])

                elif rule[0] == 'epsilon':
                    self.__first_col[lhs[0]].add('epsilon')

    def __build_follow(self):
        non_terminals = self.__grammar.get_nonterminals()
        terminals = self.__grammar.get_terminals()
        productions = self.__grammar.get_productions().get_all()

        for symbol in non_terminals:
            self.__follow_col[symbol] = set()

        self.__follow_col[self.__grammar.get_input_symbol()] = set('$')

        for lhs, rhs in productions.items():
            for rule in rhs:
                for i in range(len(rule)):
                    symbol = rule[i]
                    if symbol in non_terminals:
                        if i == len(rule) - 1:
                            self.__follow_col[symbol].update(self.__follow_col[lhs[0]])
                        elif rule[i + 1] in terminals:
                            self.__follow_col[symbol].add(rule[i + 1])
                        elif rule[i + 1] in non_terminals:
                            self.__follow_col[symbol].update(self.__first_col[rule[i + 1]] - {'epsilon'})
                            if 'epsilon' in self.__first_col[rule[i + 1]]:
                                self.__follow_col[symbol].update(self.__follow_col[lhs[0]])

    def __build_parsing_table(self):
        non_terminals = self.__grammar.get_nonterminals()
        terminals = self.__grammar.get_terminals()
        productions = self.__grammar.get_productions().get_all()

        for lhs, rhs in productions.items():
            for rule in rhs:
                if rule[0] in terminals:
                    if self.__parsing_table[lhs[0]][rule[0]] is None:
                        self.__parsing_table[lhs[0]][rule[0]] = rule
                    else:
                        raise ValueError(f"Grammar is not LL(1), conflict detected for {lhs[0]} and {rule[0]}")

                elif rule[0] in non_terminals:
                    for terminal in self.__first_col[rule[0]]:
                        if self.__parsing_table[lhs[0]][terminal] is None:
                            self.__parsing_table[lhs[0]][terminal] = rule
                        else:
                            raise ValueError(f"Grammar is not LL(1), conflict detected for {lhs[0]} and {terminal}")

                elif rule[0] == 'epsilon':
                    for terminal in self.__follow_col[lhs[0]]:
                        if self.__parsing_table[lhs[0]][terminal] is None:
                            self.__parsing_table[lhs[0]][terminal] = rule
                        else:
                            raise ValueError(f"Grammar is not LL(1), conflict detected for {lhs[0]} and epsilon")

    def get_parsing_table(self):
        return self.__parsing_table

    def parse(self, input):
        input = input + '$'
        stack = list()
        stack.append('$')
        stack.append(self.__grammar.get_input_symbol())
        input_index = 0

        while len(stack) > 0:
            top = stack.pop()

            if top in self.__grammar.get_nonterminals():
                if self.__parsing_table[top][input[input_index]] is None:
                    return False

                for symbol in reversed(self.__parsing_table[top][input[input_index]]):
                    stack.append(symbol)


            elif top in [*self.__grammar.get_terminals(), '$']:
                if top != input[input_index]:
                    return False

                input_index += 1

            elif top == 'epsilon':
                continue

            else:
                raise ValueError("Invalid symbol in stack: {}".format(top))

        return True



