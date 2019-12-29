from .Token import Token
from .Error import UnclassifiedTokenError


class Lexer:
    """ Compiler toolchain element """

    def __init__(self, error_emitter):
        self.error_emitter = error_emitter

    def parse(self, text):
        """ Split text into tokens """

        i = 0
        tokens = []

        while i < len(text):
            token, length = Token.classificate(text[i:])
            if token is not None:
                tokens.append((token, length))
                i += length
            else:
                self.error_emitter.emit(UnclassifiedTokenError(i, token))
                i += i

        return tokens
