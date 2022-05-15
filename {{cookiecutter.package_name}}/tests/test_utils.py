from {{ cookiecutter.package_name }}.utils import example_function


class TestUtils:
    def test_example_function(self):
        assert example_function(1, 1)
        assert example_function(2.0, 2.0)
        assert example_function(3, 3.0)
        assert example_function(4.00000000000000001, 4.0)
        assert not example_function(-1, 1)
        assert not example_function(1.0, 2.0)
        assert not example_function(2.0, 3)
        assert not example_function(4.0001, 4.0)
