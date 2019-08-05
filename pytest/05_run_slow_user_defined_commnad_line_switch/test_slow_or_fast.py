
# content of test_module.py
import pytest


slow = pytest.mark.skipif(
    not pytest.config.getoption("--runslow"),
    reason="need --runslow option to run"
)


def test_func_fast():
    pass


@slow
def test_func_slow():
    pass


# pytest --junit-xml=junit.xml -v --runslow
