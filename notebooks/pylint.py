"""Pylint examples.

https://pylint.readthedocs.io/en/latest/user_guide/messages/error/return-outside-function.html
https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/no-else-return.html
"""


def is_john(name):
    """Check if name is 'john' or 'John'."""
    if name.lower() == "john":
        return True
    else:
        return False
