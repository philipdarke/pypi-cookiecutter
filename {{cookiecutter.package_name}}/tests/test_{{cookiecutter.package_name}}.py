from {{ cookiecutter.package_name }} import ExampleClass


class TestExampleClass:
    def test_example_method(self):
        test = ExampleClass("4", 5, 6.0)
        assert test.example_method("4")
        assert test.example_method(5)
        assert test.example_method(6.0)
        assert not test.example_method(7)
