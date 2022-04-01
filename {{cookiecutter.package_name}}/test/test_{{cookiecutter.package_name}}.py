import {{cookiecutter.package_name}}


class TestExamples:
    def test_function(self):
        assert {{cookiecutter.package_name}}.a_function(1, 2)

    def test_class(self):
        a_class = {{cookiecutter.package_name}}.AClass(1, 2, 3)
        assert a_class.a_method(3, 4)
