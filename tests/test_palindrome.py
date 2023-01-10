"""
Credit: https://realpython.com/pytest-python-testing/
"""
import pytest


def is_palindrome(string):
    return string == string[::-1]


def canonicalize(string):
    return string.lower().replace(" ", "").replace("?", "")


@pytest.mark.parametrize(
    "palindrome",
    [
        "",
        "a",
        "Bob",
        "Never odd or even",
        "Do geese see God?",
    ],
)
def test_is_palindrome(palindrome):
    canonicalized = canonicalize(palindrome)

    assert is_palindrome(canonicalized)


@pytest.mark.parametrize(
    "non_palindrome",
    [
        "abc",
        "abab",
        "This is definitely not a palindrome!",
    ],
)
def test_is_palindrome_not_palindrome(non_palindrome):
    canonicalized = canonicalize(non_palindrome)

    assert not is_palindrome(canonicalized)


def test_is_palindrome_raises_type_error():
    with pytest.raises(TypeError):
        is_palindrome(123)
