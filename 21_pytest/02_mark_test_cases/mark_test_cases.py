
import pytest


def is_blue():
    return True


def is_stored_correctly():
    return False


@pytest.mark.frontend
def test_something_is_blue():
    pytest.assume(is_blue(), 'Message if not blue')


@pytest.mark.backend
def test_data_is_stored_correctly():
    pytest.assume(is_stored_correctly(), 'Message for not storing correctly')


# Calling:
# -m switch for filtering by marker
# without any filter pytest will execute all test cases
#
# pytest -m frontend
# will execute test cases which marked with frontend
#
# pytest -m backend
# will execute test cases which marked with backend
