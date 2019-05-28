
import pytest

########################################################################
#                                                                      #
# Defining setup and teardown functions                                #
#                                                                      #
########################################################################


# Old style


def setup_module():
    print('\n----------- setup_module ----------------\n')


def teardown_module():
    print('\n----------- teardown_module -------------\n')


def setup_function():
    print('\n------------- setup_function ------------------\n')


def teardown_function():
    print('\n------------- teardown_function ---------------\n')


# New style, but they can be combined


@pytest.fixture(scope='function')
def setup_function_type_a():
    print('\n--------------- setup function type A -----------------\n')
    yield
    print('\n--------------- teardown function type A -----------------\n')


@pytest.fixture(scope='function')
def setup_function_type_b():
    print('\n--------------- setup function type B -----------------\n')
    yield
    print('\n--------------- teardown function type B -----------------\n')


########################################################################
#                                                                      #
# Defining test cases                                                  #
#                                                                      #
########################################################################


@pytest.mark.usefixtures('setup_function_type_a')
def test_with_setup_a():
    print('\n----------------- test function uses type A setup and teardown ------------------\n')


@pytest.mark.usefixtures('setup_function_type_b')
def test_with_setup_b():
    print('\n----------------- test function uses type B setup and teardown ------------------\n')


########################################################################
#                                                                      #
# Result output                                                        #
#                                                                      #
########################################################################

'''
test_with_setup_teardown.py
----------- setup_module ----------------

------------- setup_function ------------------
--------------- setup function type A -----------------
----------------- test function uses type A setup and teardown ------------------
--------------- teardown function type A -----------------
------------- teardown_function ---------------

------------- setup_function ------------------
--------------- setup function type B -----------------
----------------- test function uses type B setup and teardown ------------------
--------------- teardown function type B -----------------
------------- teardown_function ---------------

----------- teardown_module -------------
'''


