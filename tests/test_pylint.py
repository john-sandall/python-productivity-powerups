"""Example test."""
import pytest

from notebooks.pylint import is_john


def test_is_john():
    """Test the is_john() function."""
    assert is_john("John") is True
    assert is_john("JOHN") is True
    assert is_john("john") is True
    assert is_john("Coefficient") is False

    with pytest.raises(AttributeError):
        is_john(123)
