import unittest
from app.core.lexer import Token


class TokenTestCase(unittest.TestCase):
    def test_classification_symbol(self):
        self.assertEqual(Token.classificate('$'), (Token.Symbol, 1))

    def test_classification_identifier(self):
        self.assertEqual(Token.classificate('test_test'), (Token.Identifier, 9))
        self.assertEqual(Token.classificate('digit_5'), (Token.Identifier, 7))

    def test_classification_number(self):
        self.assertEqual(Token.classificate('2fH'), (Token.Number, 3))
        self.assertEqual(Token.classificate('010101B'), (Token.Number, 7))

    def test_classification_string(self):
        self.assertEqual(Token.classificate('"quoted " string"'), (Token.String, 17))
        self.assertEqual(Token.classificate('"quoted " string" ignore'), (Token.String, 17))

    def test_classification_comment(self):
        self.assertEqual(Token.classificate(';this is a comment'), (Token.Comment, 18))


if __name__ == '__main__':
    unittest.main()
