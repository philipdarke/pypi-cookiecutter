# Based on https://www.sphinx-doc.org/en/master/usage/extensions/example_google.html


def a_function(param1: int, param2: str) -> bool:
    """Lorem ipsum dolor sit amet, consectetur adipiscing elit.

    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip
    ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit
    esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
    proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

    Args:
        param1: Description of the first parameter.
        param2: Description of the second parameter.

    Returns:
        bool: True if successful, False otherwise.

    """
    return True


class AClass:
    """Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip
    ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit
    esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
    proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

    Attributes:
        attr1 (str): Description of the first attribute.
        attr2 (int): Description of the second attribute.

    """

    def __init__(self, param1: str, param2: int, param3: list):
        """Docstring on the __init__ method.

        The __init__ method may be documented in either the class level
        docstring, or as a docstring on the __init__ method itself. Either form is
        acceptable, but the two should not be mixed. Choose one convention to document
        the __init__ method and be consistent with it.

        Args:
            param1: Description of the first parameter.
            param2: Description of the second parameter.
            param3: Description of the third parameter.

        """
        self.attr1 = param1
        self.attr2 = param2
        self.param3 = param3

    def a_method(self, param1: float, param2: int) -> bool:
        """Docstring on a class method.

        Args:
            param1: Description of the first parameter.
            param2: Description of the second parameter.

        Returns:
            bool: True if successful, False otherwise.

        """
        return True
