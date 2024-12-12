from grammar import Grammar
import itertools

class Ll1:
    def __init__(self, input_file):
        self.__grammar = Grammar(input_file=input_file)
        self.__first_col = dict()
        self.__follow_col = dict()
        self.__parsing_table = dict()

        self.__build_table()

    def first(self, symbol):
        return self.__first_col[symbol]

    def follow(self, symbol):
        return self.__follow_col[symbol]

    def grammar(self):
        return self.__grammar

    def get_parsed_table(self):
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

    def __build_table(self):
        self.__build_first()
        self.__build_follow()
        self.__build_parsing_table()

    def __build_first(self):
        non_terminals = self.__grammar.get_nonterminals()
        terminals = self.__grammar.get_terminals()
        productions = self.__grammar.get_productions().get_all()
        first_col = self.__first_col

        for symbol in non_terminals:
            first_col[symbol] = set()

        for lhs, rhs in reversed(productions.items()):
            for rule in rhs:
                if rule[0] in terminals:
                    first_col[lhs[0]].add(rule[0])

                elif rule[0] in non_terminals:
                    first_col[lhs[0]] = first_col[lhs[0]].union(first_col[rule[0]])

                elif rule[0] == 'epsilon':
                    first_col[lhs[0]].add('epsilon')

                else:
                    raise ValueError("Invalid symbol in production rule: {}".format(rule[0]))

    def __build_follow(self):
        non_terminals = self.__grammar.get_nonterminals()
        terminals = self.__grammar.get_terminals()
        productions = self.__grammar.get_productions().get_all()
        first_col = self.__first_col
        follow_col = self.__follow_col

        for symbol in non_terminals:
            follow_col[symbol] = set()

        follow_col[self.__grammar.get_input_symbol()] = set('$')

        for key in productions.keys():

            for lhs, rhs in productions.items():
                for rule in rhs:
                    for i in range(len(rule)):
                        symbol = rule[i]

                        if symbol == key[0]:

                            if i == len(rule) - 1:
                                follow_col[symbol] = follow_col[symbol].union(follow_col[lhs[0]])

                            elif rule[i + 1] in terminals:
                                follow_col[symbol].add(rule[i + 1])

                            elif rule[i + 1] in non_terminals:
                                if 'epsilon' in first_col[rule[i + 1]]:
                                    follow_col[symbol] = follow_col[symbol].union(first_col[rule[i + 1]]) - {'epsilon'}
                                    follow_col[symbol] = follow_col[symbol].union(follow_col[lhs[0]])
                                else:
                                    follow_col[symbol] = follow_col[symbol].union(first_col[rule[i + 1]])

                            else:
                                raise ValueError("Invalid symbol in production rule: {}".format(rule[i + 1]))

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