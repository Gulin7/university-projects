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