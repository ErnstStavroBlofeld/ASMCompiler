from app.core.lexer import Lexer, Token
from app.core.helper import Emitter


def test_lexer_empty():
    assert Lexer(Emitter()).parse('') == []


def test_lexer_identifier_whitespace():
    assert Lexer(Emitter()).parse('this is number') == [
        (Token.Identifier, 'this'),
        (Token.Whitespace, ' '),
        (Token.Identifier, 'is'),
        (Token.Whitespace, ' '),
        (Token.Identifier, 'number')
    ]


def test_lexer_identifier_number_whitespace():
    assert Lexer(Emitter()).parse('this 533H 349 110001b 4317o') == [
        (Token.Identifier, 'this'),
        (Token.Whitespace, ' '),
        (Token.Number, '533H'),
        (Token.Whitespace, ' '),
        (Token.Number, '349'),
        (Token.Whitespace, ' '),
        (Token.Number, '110001b'),
        (Token.Whitespace, ' '),
        (Token.Number, '4317o')
    ]


def test_lexer_identifier_whitespace_string():
    assert Lexer(Emitter()).parse('test "string"') == [
        (Token.Identifier, 'test'),
        (Token.Whitespace, ' '),
        (Token.String, '"string"')
    ]


def test_lexer_identifier_comment():
    assert Lexer(Emitter()).parse('identifier ;comments with spaces') == [
        (Token.Identifier, 'identifier'),
        (Token.Whitespace, ' '),
        (Token.Comment, ';comments with spaces')
    ]


def test_lexer_comment_unicode():
    assert Lexer(Emitter()).parse(';тэѕт ẗëṡẗ') == [
        (Token.Comment, ';тэѕт ẗëṡẗ')
    ]
