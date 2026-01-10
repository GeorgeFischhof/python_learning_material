
import pytest


@pytest.mark.parametrize("test_input, expected", [
    ("3+5", 8),
    ("2+4", 6),
])
def test_eval(test_input, expected):
    assert eval(test_input) == expected


@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3])
def test_foo(x, y):
    pass

"""
pytest --verbose

test_parameters.py::test_eval[3+5-8] PASSED
test_parameters.py::test_eval[2+4-6] PASSED
test_parameters.py::test_foo[2-0] PASSED
test_parameters.py::test_foo[2-1] PASSED
test_parameters.py::test_foo[3-0] PASSED
test_parameters.py::test_foo[3-1] PASSED
"""

# Look at the output, note the order of execution in matrix
# 2-0 2-1 3-0 3-1
# the execution order of decorators are from down to top
