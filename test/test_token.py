from app.core.lexer import Token


def test_classification_identifier():
    assert Token.classificate('test_test') == (Token.Identifier, 9)


def test_classification_identifier_with_digit():
    assert Token.classificate('digit_5') == (Token.Identifier, 7)


def test_classification_identifier_and_number():
    assert Token.classificate('add 22') == (Token.Identifier, 3)


def test_classification_identifier_with_underscore_and_number():
    assert Token.classificate('_22h') == (Token.Identifier, 4)


def test_classification_number():
    assert Token.classificate('029347412') == (Token.Number, 9)


def test_classification_number_hexadecimal():
    assert Token.classificate('2fH') == (Token.Number, 3)


def test_classification_number_octal():
    assert Token.classificate('1147o') == (Token.Number, 5)


def test_classification_number_binary():
    assert Token.classificate('010101B') == (Token.Number, 7)


def test_classification_number_and_identifier():
    assert Token.classificate('3472O token') == (Token.Number, 5)


def test_classification_string_with_quote():
    assert Token.classificate('"quoted "string"') == (Token.String, 16)


def test_classification_string_with_quote_and_identifier():
    assert Token.classificate('"quoted "string" ignore') == (Token.String, 16)


def test_classification_string_nested():
    assert Token.classificate('"quoted "multiple" strings"') == (Token.String, 27)


def test_classification_string_invalid():
    assert Token.classificate('"quoted invalid string') == (Token.Symbol, 1)


def test_classification_comment():
    assert Token.classificate(';this is a comment') == (Token.Comment, 18)


def test_classification_comment_with_number():
    assert Token.classificate(';comment with number 42H') == (Token.Comment, 24)


def test_classification_whitespace_characters():
    assert Token.classificate('\r\n\t\f\v ') == (Token.Whitespace, 6)


def test_classification_whitespace_and_identifier():
    assert Token.classificate('   \ttext') == (Token.Whitespace, 4)
