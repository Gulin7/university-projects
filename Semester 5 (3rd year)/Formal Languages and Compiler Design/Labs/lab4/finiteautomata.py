import re

class FiniteAutomata:
    def __init__(self, _filename):
        self.states = []
        self.alphabet = []
        self.transitions = {}
        self.initial_state = ""
        self.final_states = []
        self.filename = _filename
        self.read_from_file()

    def read_from_file(self):
        with open(self.filename, 'r') as program:
            line_nr = 0
            is_transition = False
            for line in program:
                if line_nr == 1:
                    for state in re.split('[ ,Q=\n]', line):
                        if state != '':
                            self.states.append(state)
                if line_nr == 2:
                    for letter in re.split('[, E=\n]', line):
                        if letter != '':
                            self.alphabet.append(letter)
                if line == "start\n":
                    is_transition = True
                    continue
                if line == "end\n":
                    is_transition = False
                    continue
                if is_transition:
                    is_last = False
                    is_first = True
                    first = ""
                    last = ""
                    letters = []
                    for word in re.split('[, \[\]\n]', line):
                        if word == '':
                            continue
                        if is_first:
                            first = word
                            is_first = False
                        if is_last:
                            last = word

                        if word == "->":
                            is_last = True
                        if word != '' and word != first and word != last and word != '->':
                            letters.append(word)
                    for letter in letters:
                        self.transitions[(first, letter)] = last
                    continue
                if re.split("[= ]", line)[0] == "q0":
                    self.initial_state = re.split("[= ]", line)[3]
                    continue
                if re.split("[= ,]", line)[0] == "F":
                    for word in re.split("[= ,]", line):
                        if word == "F":
                            continue
                        if word != '':
                            self.final_states.append(word)
                    continue
                line_nr += 1

    def print_fa(self):
        print("M = {Q, E, RO, q0, F}\n")
        print(f"Q = {self.states}\n")
        print(f"E = {self.alphabet}\n")
        print(f"RO = {self.transitions}\n")
        print(f"q0 = {self.initial_state}\n")
        print(f"F = {self.final_states}\n")

    def start_menu(self):
        option = -1

        while option != 0:
            self.print_menu()
            option = int(input())
            if option == 1:
                print(f"Q = {self.states}\n")
            if option == 2:
                print(f"E = {self.alphabet}\n")
            if option == 3:
                print(f"RO = {self.transitions}\n")
            if option == 4:
                print(f"q0 = {self.initial_state}\n")
            if option == 5:
                print(f"F = {self.final_states}\n")
            if option == 6:
                if self.is_deterministic():
                    print("The finite automaton is deterministic.")
                else:
                    print("The finite automaton is not deterministic.")

    def is_deterministic(self):
        # Create a set to store (state, symbol) pairs
        seen_transitions = set()

        # Iterate over all transitions
        for (state, symbol), target_state in self.transitions.items():
            # Check for epsilon (ε) transitions
            if symbol == "" or symbol == "ε":
                print(
                    f"Non-deterministic transition detected: Epsilon (ε) transition from state '{state}' to '{target_state}'.")
                return False

            # Check if the (state, symbol) pair is already in the set
            if (state, symbol) in seen_transitions:
                print(
                    f"Non-deterministic transition detected: State '{state}' has multiple transitions for symbol '{symbol}'.")
                return False

            # Add the (state, symbol) pair to the set
            seen_transitions.add((state, symbol))

        # If no epsilon transitions and no duplicate (state, symbol) pairs are found, it is deterministic
        print("The finite automaton is deterministic.")
        return True

    def print_menu(self):
        print("press 0 to exit")
        print("press 1 for set of states")
        print("press 2 for alphabet")
        print("press 3 for set of transitions")
        print("press 4 for initial state")
        print("press 5 for final states")
        print("press 6 to check if the finite automaton is deterministic")

    def check_word_if_integer_constant(self, word):
        state = 'q0'
        for letter in word:
            state = self.transitions.get((state, letter))
            if state is None:
                return

        if state not in ['q5', 'q6']:
            return False
        return True

    def check_word_if_identifier(self, word):
        state = 'q0'
        for letter in word:
            state = self.transitions.get((state, letter))
            if state is None:
                return

        if state not in ['q2']:
            return False
        return True