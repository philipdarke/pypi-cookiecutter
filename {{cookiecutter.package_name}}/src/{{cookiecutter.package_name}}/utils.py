"""Add an introduction to each module in ``[module_name].py``.
"""


def example_function(a: float, b: float, eps: float = 1e-8) -> bool:
    r"""Example function that determines whether two input numbers ``a`` and ``b`` are
    equal i.e. whether

    .. math:: a = b

    Parameters:
        a: First number.
        b: Second number.
        eps: Tolerance for float calculations (default 1 x 10\ :sup:`-8`)

    Returns:
        True if inputs are equal, else False.

    """
    return abs(a - b) < eps
