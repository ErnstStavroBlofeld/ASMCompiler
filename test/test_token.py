from app.core.lexer import Token


def test_classification_symbol():
    assert Token.classificate('$') == (Token.Symbol, 1)
    assert Token.classificate('#') == (Token.Symbol, 1)
    assert Token.classificate('*') == (Token.Symbol, 1)


def test_classification_identifier():
    assert Token.classificate('test_test') == (Token.Identifier, 9)
    assert Token.classificate('digit_5') == (Token.Identifier, 7)
    assert Token.classificate('add 22') == (Token.Identifier, 3)
    assert Token.classificate('_22h') == (Token.Identifier, 4)


def test_classification_number():
    assert Token.classificate('2fH') == (Token.Number, 3)
    assert Token.classificate('1147o') == (Token.Number, 5)
    assert Token.classificate('010101B') == (Token.Number, 7)
    assert Token.classificate('3472O token') == (Token.Number, 5)


def test_classification_string():
    assert Token.classificate('"quoted " string"') == (Token.String, 17)
    assert Token.classificate('"quoted " string" ignore') == (Token.String, 17)
    assert Token.classificate('"quoted "multiple" strings"') == (Token.String, 27)


def test_classification_comment():
    assert Token.classificate(';this is a comment') == (Token.Comment, 18)
    assert Token.classificate(';comment with number 42H') == (Token.Comment, 24)


def test_classification_whitespace():
    assert Token.classificate('\r\n\t\f\v ') == (Token.Whitespace, 6)
    assert Token.classificate('   \ttext') == (Token.Whitespace, 4)
