import os

from FiniteAutomaton import FiniteAutomaton
from MyScanner import MyScanner


def print_to_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(str(content))
    except FileNotFoundError as e:
        print(f"File not found: {e}")

def run(file_path):
    scanner = MyScanner(file_path)
    scanner.scan()
    st_file_path = file_path.replace(".txt", "ST.txt")
    pif_file_path = file_path.replace(".txt", "PIF.txt")
    print_to_file(st_file_path, scanner.get_symbol_table().get_hash_table())
    print_to_file(pif_file_path, scanner.get_pif())

def print_menu():
    print("1. Display states")
    print("2. Display alphabet")
    print("3. Display final states")
    print("4. Display transitions")
    print("5. Display initial state")
    print("6. Check if deterministic")
    print("7. Check if a sequence is accepted by DFA")
    print("0. Return to main menu")

def main_menu():
    print("1. Finite Automaton operations")
    print("2. Run Scanner on predefined files")
    print("0. Exit")


def options_for_dfa():
    file_path = "InOut/FA.txt"

    if not os.path.isfile(file_path):
        print(f"File '{file_path}' not found.")
        return

    finite_automaton = FiniteAutomaton(file_path)
    print("Finite Automaton read from file.")

    while True:
        print_menu()
        option = input("Your option: ")

        if option == '0':
            print("Exiting DFA options.")
            break

        elif option == '1':
            print("States:")
            print(finite_automaton.get_states())
            print()

        elif option == '2':
            print("Alphabet:")
            print(finite_automaton.get_alphabet())
            print()

        elif option == '3':
            print("Final states:")
            print(finite_automaton.get_final_states())
            print()

        elif option == '4':
            print("Transitions:")
            print(finite_automaton.write_transitions())
            print()

        elif option == '5':
            print("Initial state:")
            print(finite_automaton.get_initial_state())
            print()

        elif option == '6':
            print("Is deterministic?")
            print(finite_automaton.check_if_deterministic())
            print()

        elif option == '7':

            sequence = input("Enter your sequence: ")
            if finite_automaton.accepts_sequence(sequence):
                print("Sequence is valid.")
            else:
                print("Invalid sequence.")
            print()

        else:
            print("Invalid command! Please try again.")
            print()


def run_scanner():
    run("InOut/p1.txt")
    run("InOut/p2.txt")
    run("InOut/p3.txt")
    run("InOut/p1err.txt")


def main():
    main_menu()
    option = input("Enter your choice: ")

    if option == '1':
        options_for_dfa()
    elif option == '2':
        run_scanner()
    else:
        print("Invalid command! Please try again.")


if __name__ == "__main__":
    main()