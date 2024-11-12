from HashTable import HashTable, Pair


class SymbolTable:
    def __init__(self,size):
        self.hash_table=HashTable(size)

    def find_by_position(self, pos):
        return self.hash_table.find_by_position(pos)

    def get_hash_table(self):
        return self.hash_table

    def get_size(self):
        return self.hash_table.get_size()

    def find_position_of_term(self, e):
        return self.hash_table.find_pos(e)

    def contains_elem(self, e):
        return self.hash_table.contains_elem(e)

    def add(self, e):
        return self.hash_table.add(e)

