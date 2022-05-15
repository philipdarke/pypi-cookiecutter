import {{ cookiecutter.package_name }}


class TestExamples:
    def test_a_utility_function(self):
        assert {{ cookiecutter.package_name }}.a_utilityfunction(1, 2)
