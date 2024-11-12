from typing import List, Dict, Set, Tuple

class FiniteAutomaton:
    def __init__(self, file_path: str):
        self.elem_separator = "."
        self.states: List[str] = []
        self.initial_state: str = ""
        self.alphabet: List[str] = []
        self.final_states: List[str] = []
        self.transitions: Dict[Tuple[str, str], Set[str]] = {}

        self.is_deterministic = self.read_from_file(file_path)

    def read_from_file(self, file_path: str) -> bool:
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()

                if len(lines) < 4:
                    raise ValueError("File does not contain enough lines for states, initial state, alphabet, and final states.")


                self.states = lines[0].strip().split(self.elem_separator)
                self.initial_state = lines[1].strip()
                self.alphabet = lines[2].strip().split(self.elem_separator)
                self.final_states = lines[3].strip().split(self.elem_separator)


                for line in lines[4:]:
                    transition_components = line.strip().split(" ")
                    if len(transition_components) != 3:
                        print(f"Invalid transition line: {line.strip()}")
                        continue

                    start_state, symbol, end_state = transition_components
                    if start_state in self.states and end_state in self.states and symbol in self.alphabet:
                        key = (start_state, symbol)
                        if key not in self.transitions:
                            self.transitions[key] = set()
                        self.transitions[key].add(end_state)

            return self.check_if_deterministic()

        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return False
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            return False

    def check_if_deterministic(self):
        return all(len(destinations) <= 1 for destinations in self.transitions.values())

    def write_transitions(self):
        builder = []
        builder.append("Transitions:")
        for (start_state, symbol), end_states in self.transitions.items():
            builder.append(f"<{start_state}, {symbol}> -> {list(end_states)}")
        return "\n".join(builder)

    def accepts_sequence(self, sequence: str) -> bool:
        if not self.is_deterministic:
            print("The automaton is non-deterministic and cannot process the sequence deterministically.")
            return False

        current_state = self.initial_state
        for symbol in sequence:
            key = (current_state, symbol)
            if key in self.transitions and len(self.transitions[key]) == 1:
                current_state = next(iter(self.transitions[key]))
            else:
                return False

        return current_state in self.final_states


    def get_states(self) -> List[str]:
        return self.states

    def get_initial_state(self) -> str:
        return self.initial_state

    def get_alphabet(self) -> List[str]:
        return self.alphabet

    def get_final_states(self) -> List[str]:
        return self.final_states

    def get_transitions(self) -> Dict[Tuple[str, str], Set[str]]:
        return self.transitions
