class ExampleClass:
    """Example class.

    Sed nulla augue, sagittis vel consequat non, posuere sit amet nibh. Aenean et tempor
    metus. Proin dignissim aliquam scelerisque. Proin sit amet eleifend sem. Vivamus
    sodales, justo a lacinia accumsan, augue orci gravida metus, lobortis posuere massa
    dolor in nisi. Maecenas dictum odio eget leo tincidunt, et tempor felis
    sollicitudin.

    .. warning::
        Quisque bibendum justo auctor enim accumsan, eget sodales arcu gravida.

    Parameters:
        x: First input.
        y: Second input.
        z: Third input.

    Attributes:
        tokens: List of all class parameters.
    """

    def __init__(self, x: str, y: int, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

        self.tokens = [x, y, z]

    def example_method(self, input: float) -> bool:
        """Example method.

        Parameters:
            input: Numeric input for testing.

        Returns:
            bool: True if ``input`` matches a class parameter, otherwise False.

        """
        return input in self.tokens
