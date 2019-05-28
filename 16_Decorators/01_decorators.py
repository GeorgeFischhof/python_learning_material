
# https://realpython.com/primer-on-python-decorators/

from functools import wraps


def decorator_function_like_a_shell(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('I am the decorator -- First part of the shell')

        # Call the decorated function
        result = func(*args, **kwargs)

        print('I am the decorator -- Last part of the shell')

        return result
    return wrapper


@decorator_function_like_a_shell
def function_to_be_executed_within_decorator(parameter):
    print('I am the decorated function, my parameter: {parameter}'.format(parameter=parameter))
    return parameter


if __name__ == '__main__':
    function_result = function_to_be_executed_within_decorator(123)
    print('Result from decorated function call: {result} \n'.format(result=function_result))

    function_result = function_to_be_executed_within_decorator(parameter='abc')
    print('Result from decorated function call: {result}'.format(result=function_result))
