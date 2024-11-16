class ProgramInternalForm:
    def __init__(self):
        self.tokenPositionPair = []
        self.types = []
        #types:
        #0-constant
        #1-Identifier
        #2-Reserved Words
        #3-Operators
        #4-Separators

    def add(self, token_position_pair, token_type):
        self.tokenPositionPair.append(token_position_pair)
        self.types.append(token_type)

    def __str__(self):
        result = []
        for i in range(len(self.tokenPositionPair)):
            token, position = self.tokenPositionPair[i]
            token_type = self.types[i]
            result.append(f"{token} - {position} -> {token_type}")
        return "\n".join(result)

