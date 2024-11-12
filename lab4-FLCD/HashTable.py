class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def get_first(self):
        return self.first
    def get_second(self):
        return self.second
    def __str__(self):
        return f"Pair({self.first}, {self.second})"

class HashTable:
    def __init__(self,size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def find_by_position(self,pos):
        if pos.first >= len(self.table) or pos.second >= len(self.table[pos.first]):
            return "No element on this position"
        return self.table[pos.get_first()][pos.get_second()]

    def find_pos(self,e):
        pos=self.hash(e)
        elems=self.table[pos]

        for i,elem in enumerate(elems):
            if elem==e:
                return Pair(pos,i)
        return None


    def get_size(self):
        return self.size

    def hash(self,key):
        sum_chars = sum(ord(c) for c in key)
        return sum_chars % self.size

    def contains_elem(self,e):
        return self.find_pos(e) is not None

    def add(self,e):
        if self.contains_elem(e):
            return False

        pos=self.hash(e)
        self.table[pos].append(e)

    def __str__(self):
        return f"SymbolTable {{ elements={self.table}, size={self.size} }}"


