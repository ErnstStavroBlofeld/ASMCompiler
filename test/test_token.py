from app.core.lexer import Token


def test_classification_symbol():
    assert Token.classificate('$') == (Token.Symbol, 1)
    assert Token.classificate('#') == (Token.Symbol, 1)


def test_classification_identifier():
    assert Token.classificate('test_test') == (Token.Identifier, 9)
    assert Token.classificate('digit_5') == (Token.Identifier, 7)


def test_classification_number():
    assert Token.classificate('2fH') == (Token.Number, 3)
    assert Token.classificate('010101B') == (Token.Number, 7)


def test_classification_string():
    assert Token.classificate('"quoted " string"') == (Token.String, 17)
    assert Token.classificate('"quoted " string" ignore') == (Token.String, 17)


def test_classification_comment():
    assert Token.classificate(';this is a comment') == (Token.Comment, 18)
