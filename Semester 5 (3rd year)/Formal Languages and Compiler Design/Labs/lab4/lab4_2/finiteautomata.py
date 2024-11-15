import re


class FiniteAutomaton:
    def __init__(self, filename):
        self.states = []
        self.alphabet = []
        self.transitions = {}
        self.initial_state = ""
        self.final_states = []
        self.filename = filename
        self._read_from_file()

    def _read_from_file(self):
        """Reads the FA specification from a file."""
        with open(self.filename, 'r') as file:
            lines = file.readlines()

        # Parse the states, alphabet, and other components
        self.states = self._parse_line(lines[1], r'[ ,Q=\n]')
        self.alphabet = self._parse_line(lines[2], r'[, E=\n]')

        is_transition_section = False
        for line in lines[3:]:
            line = line.strip()

            if line == "start":
                is_transition_section = True
                continue
            if line == "end":
                is_transition_section = False
                continue

            if is_transition_section:
                self._parse_transition(line)
            elif "q0" in line:
                self.initial_state = self._extract_value(line)
            elif "F" in line:
                self.final_states = self._parse_line(line, r'[= ,]')

    def _parse_line(self, line, pattern):
        """Helper function to parse lists (states, alphabet, final states)."""
        return [item for item in re.split(pattern, line) if item]

    def _parse_transition(self, line):
        """Parse a transition line and store it in the transitions dictionary."""
        parts = re.split(r'[,\[\]\s]+', line)
        state, symbol, target_state = None, None, None
        transition_started = False

        for part in parts:
            if part == '->':
                transition_started = True
            elif transition_started:
                target_state = part
            else:
                if not state:
                    state = part
                else:
                    symbol = part

        if state and symbol and target_state:
            self.transitions[(state, symbol)] = target_state

    def print_fa(self):
        """Print the finite automaton components."""
        print("M = {Q, E, RO, q0, F}\n")
        print(f"Q = {self.states}")
        print(f"E = {self.alphabet}")
        print(f"RO = {self.transitions}")
        print(f"q0 = {self.initial_state}")
        print(f"F = {self.final_states}")

    def start_menu(self):
        """Start the interactive menu."""
        option = -1
        while option != 0:
            self.print_menu()
            try:
                option = int(input())
                self._handle_menu_option(option)
            except ValueError:
                print("Invalid input, please enter a valid option.")

    def _handle_menu_option(self, option):
        """Handle different menu options."""
        if option == 1:
            print(f"Q = {self.states}")
        elif option == 2:
            print(f"E = {self.alphabet}")
        elif option == 3:
            print(f"RO = {self.transitions}")
        elif option == 4:
            print(f"q0 = {self.initial_state}")
        elif option == 5:
            print(f"F = {self.final_states}")
        elif option == 6:
            self.check_deterministic()
        elif option == 0:
            print("Exiting menu.")
        else:
            print("Invalid option. Please choose again.")

    def print_menu(self):
        """Print the menu options."""
        print("Press 0 to exit")
        print("Press 1 for set of states")
        print("Press 2 for alphabet")
        print("Press 3 for set of transitions")
        print("Press 4 for initial state")
        print("Press 5 for final states")
        print("Press 6 to check if the finite automaton is deterministic")

    def check_deterministic(self):
        """Check if the finite automaton is deterministic."""
        seen_transitions = set()
        for (state, symbol), target_state in self.transitions.items():
            if (symbol == "" or symbol == "ε"):
                print(
                    f"Non-deterministic transition detected: Epsilon (ε) transition from state '{state}' to '{target_state}'.")
                return False
            if (state, symbol) in seen_transitions:
                print(
                    f"Non-deterministic transition detected: State '{state}' has multiple transitions for symbol '{symbol}'.")
                return False
            seen_transitions.add((state, symbol))

        print("The finite automaton is deterministic.")
        return True

    def check_word_if_integer_constant(self, word):
        """Check if the word matches the integer constant pattern."""
        state = 'q0'
        for letter in word:
            state = self.transitions.get((state, letter))
            if state is None:
                return False
        return state in ['q5', 'q6']

    def check_word_if_identifier(self, word):
        """Check if the word matches the identifier pattern."""
        state = 'q0'
        for letter in word:
            state = self.transitions.get((state, letter))
            if state is None:
                return False
        return state == 'q2'
