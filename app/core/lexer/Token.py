from enum import Enum
from re import search


def match_length(regex, sequence):
    """ Return length of regex match or 0 if none matched """

    result = search(regex, sequence)
    return result.span()[1] if result is not None else 0


class Token(Enum):
    """ Character sequence representation """

    Letter = (1, lambda char: match_length(r'[A-Za-z]', char))
    Digit = (1, lambda char: match_length(r'[0-9]', char))
    Symbol = (1, lambda char: match_length(r'[#;:,"+-/*@~=<>$]', char))
    Identifier = (100, lambda seq: match_length(r'[A-Za-z_.][A-Za-z0-9_.]*', seq))
    Number = (18, lambda seq: match_length(r'[01]+[bB]|[0-7]+[oO]|[0-9a-fA-F]+[hH]', seq))
    String = (250, lambda seq: match_length(r'".*"', seq))
    Comment = (500, lambda seq: match_length(r';.*', seq))

    def __init__(self, max_length, matcher):
        self.max_length = max_length
        self.matcher = matcher

    def __str__(self):
        return self.name

    @staticmethod
    def classificate(sequence):
        """ Match best token for given string """

        highest_token, highest_length = None, None

        for token in Token:
            length = token.matcher(sequence[:token.max_length])
            if length >= 1:
                highest_token = token
                highest_length = length

        return highest_token, highest_length
