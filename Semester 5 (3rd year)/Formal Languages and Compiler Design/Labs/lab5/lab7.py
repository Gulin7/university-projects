class ParserOutput:
    def __init__(self, parsing_table):
        self.parsing_table = parsing_table
        self.representation = self.transform_parsing_table_into_representation()

    def transform_parsing_table_into_representation(self):
        representation = []
        for non_terminal, rules in self.parsing_table.items():
            for terminal, rule in rules.items():
                if rule is not None:
                    father = non_terminal
                    sibling = terminal
                    representation.append((father, sibling, rule))
        return representation

    def print_to_screen(self):
        for father, sibling, rule in self.representation:
            print(f'Father: {father}, Sibling: {sibling}, Rule: {rule}')

    def print_to_file(self, filename):
        with open(filename, 'w') as file:
            for father, sibling, rule in self.representation:
                file.write(f'Father: {father}, Sibling: {sibling}, Rule: {rule}\n')

 def __build_parsing_table(self):
        non_terminals = self.__grammar.get_nonterminals()
        terminals = self.__grammar.get_terminals()
        productions = self.__grammar.get_productions().get_all()

        for non_terminal in non_terminals:
            self.__parsing_table[non_terminal] = dict()

            for terminal in terminals:
                self.__parsing_table[non_terminal][terminal] = None

            self.__parsing_table[non_terminal]['$'] = None

        for lhs, rhs in productions.items():
            for rule in rhs:

                if rule[0] in terminals:
                    if self.__parsing_table[lhs[0]][rule[0]] is not None:
                        raise ValueError(rule[0] + " Grammar is not LL(1)")

                    self.__parsing_table[lhs[0]][rule[0]] = rule

                elif rule[0] in non_terminals:
                    for terminal in self.__first_col[rule[0]]:
                        if self.__parsing_table[lhs[0]][terminal] is not None:
                            raise ValueError(rule[0] + " Grammar is not LL(1)")

                        self.__parsing_table[lhs[0]][terminal] = rule

                elif rule[0] == 'epsilon':
                    for terminal in self.__follow_col[lhs[0]]:

                        if self.__parsing_table[lhs[0]][terminal] is not None:
                            raise ValueError(rule[0] + " Grammar is not LL(1)")

                        self.__parsing_table[lhs[0]][terminal] = rule

                else:
                    raise ValueError("Invalid symbol in production rule: {}".format(rule[0]))

