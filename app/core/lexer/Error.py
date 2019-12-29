class UnclassifiedTokenError(Exception):
    def __init__(self, position, char):
        self.position = position
        self.char = char
