import pytest
from string_utils import StringUtils

string_utils = StringUtils()

# Первая буква становиться заглавной.


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("liza", "Liza"),
    ("hello world", "Hello world"),
    ("a", "A"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    (" ", " "),
    ("6lisichka", "6lisichka"),
    ("25 july", "25 july"),
    ("", "")
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
def test_capitalize_none():
    with pytest.raises(AttributeError):
        string_utils.capitalize(None)

# удаляет пробелы в начале, если они есть.


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" ", ""),
    ("   6lisichka", "6lisichka"),
    (" rok ", "rok "),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("\tskypro", "skypro"),
    ("\nskypro", "skypro"),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
def test_trim_none():
    with pytest.raises(AttributeError):
        string_utils.trim(None)

# Возвращает `True`, если строка содержит искомый символ и `False` - если нет


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("Books", "B", True),
    ("cmd", "cmd", True),
    ("hello!", "?", False),
    ("4568", "2", False),
    ("hello world", " ", True),
    ("nospace", " ", False),
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("cmd", "", True),
    ("", "h", False),
    ("", "", True),
])
def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.negative
def test_contains_none_symbol():
    with pytest.raises(TypeError):
        string_utils.contains("cmd", None)

# Удаляет все подстроки из переданной строки.


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("cmd", "m", "cd"),
    ("lisichka", "ichka", "lis"),
    ("asdasd", "as", "dd"),
    ("4562", "56", "42"),
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("cmd", "", "cmd"),
    (" ", " ", ""),
    ("Liza", "m", "Liza"),
])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
def test_delete_symbol_none_symbol():
    with pytest.raises(TypeError):
        string_utils.delete_symbol("cmd", None)
