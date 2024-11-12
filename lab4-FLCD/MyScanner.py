import re
from typing import List, Tuple

from ProgramInternalForm import ProgramInternalForm
from SymbolTable import SymbolTable


class MyScanner:
    def __init__(self, file_path: str):
        self.operators = ["+", "-", "*", "/", "%", "<=", ">=", "==", "!=", "<", ">", "<-"]
        self.separators = ["{", "}", "/", "[", "]", ":", ".", " ", ",", "\t", "\n", "'", "\""]
        self.reserved_words = [
            "mod", "add", "sub", "div", "read", "write", "if", "else", "for", "while", "int", "string", "char",
            "return", "array", "do", "show", "insert_by_user", "and", "or", "float", "range", '"-inf"',  '"inf"'
        ]
        self.file_path = file_path
        self.symbol_table = SymbolTable(50)
        self.pif = ProgramInternalForm()

    def read_file(self) -> str:
        with open(self.file_path, 'r') as file:
            return file.read().replace("\t", "")

    def create_list_of_program_elems(self) -> List[Tuple[str, Tuple[int, int]]]:
        try:
            content = self.read_file()
            separators_string = "".join(self.separators)
            tokens = re.split(f"([{re.escape(separators_string)}])", content)
            tokens = [token for token in tokens if token]
            return self.tokenize(tokens)
        except FileNotFoundError:
            print("File not found.")
            return []

    def tokenize(self, tokens_to_be: List[str]) -> List[Tuple[str, Tuple[int, int]]]:
        resulted_tokens = []
        is_string_constant = False
        is_char_constant = False
        created_string = []
        number_line = 1
        number_column = 1
        tokens_iter = iter(tokens_to_be)

        for token in tokens_to_be:
            if token == "\"":
                while True:
                    token = next(tokens_iter, None)
                    if token is None or token == "\"":
                        break
                    created_string.append(token)
                if token == "\"":
                    created_string.append(token)
                else:
                   print(f"Error: unmatched quote at line {number_line}, column {number_column}")
                is_string_constant = not is_string_constant
            elif token == "'":
                if is_char_constant:
                    created_string.append(token)
                    resulted_tokens.append(("".join(created_string), (number_line, number_column)))
                    created_string.clear()
                else:
                    created_string.append(token)
                is_char_constant = not is_char_constant
            elif token == "\n":
                number_line += 1
                number_column = 1
            else:
                if is_string_constant or is_char_constant:
                    created_string.append(token)
                elif token.strip():
                    resulted_tokens.append((token, (number_line, number_column)))
                    number_column += 1
        return resulted_tokens

    def scan(self):
        tokens = self.create_list_of_program_elems()
        lexical_error_exists = False

        for token, (line, col) in tokens:
            if token in self.reserved_words:
                self.pif.add((token, (-1, -1)), 2)
            elif token in self.operators:
                self.pif.add((token, (-1, -1)), 3)
            elif token in self.separators:
                self.pif.add((token, (-1, -1)), 4)
            elif re.match(r"^0$|[-+]?[1-9]\d*$|'[a-zA-Z0-9]'|\"[a-zA-Z0-9 ]*\"$", token):
                self.symbol_table.add(token)
                self.pif.add(("Const", self.symbol_table.find_position_of_term(token)), 0)
            elif re.match(r"^([a-zA-Z_][a-zA-Z_0-9]*)$", token):
                self.symbol_table.add(token)
                self.pif.add(("Identifier", self.symbol_table.find_position_of_term(token)), 1)
            else:
                print(f"File:{self.file_path}   Error at line: {line}, column: {col}, invalid token: '{token}'")
                lexical_error_exists = True

        if not lexical_error_exists:
            print(f"Program {self.file_path} is lexically correct!")

    def get_pif(self) -> ProgramInternalForm:
        return self.pif

    def get_symbol_table(self) -> SymbolTable:
        return self.symbol_table
