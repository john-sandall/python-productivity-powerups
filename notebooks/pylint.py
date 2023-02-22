"""Pylint examples."""


def is_john(name):
    """Check if name is 'john' or 'John'."""
    if name.lower() == "john":
        return True
    else:
        return False
