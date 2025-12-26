# Conditions

A program sometimes has to make decisions based on certain conditions and execute different code accordingly.

In Python, the `if` statement is used for conditional execution.

## if statement

```python
if expression_is_true:
    code_part_for_true_expression
```

## if ... else statement

```python
if expression_is_true:
    code_part_for_true_expression
else:
    code_part_for_false_expression
```

## Nested if statements, else if is shortened as `elif`

```python
if expression_one_is_true:
    code_part_for_true_expression_one
elif expression_two_is_true:
    code_part_for_false_expression_one_and_true_expression_two
else:
    code_part_for_false_expression_one_and_false_expression_two
```

## The boolean expression

The expression can be a single boolean variable (its value is `True` or `False`), the result of a function call,
a comparator expression, or anything that is evaluated to `True` or `False`.

### Comparators

| description              | operator |
|--------------------------|----------|
| equal to                 | `==`     |
| not equal to             | `!=`     |
| greater than             | `>`      |
| smaller than             | `<`      |
| greater than or equal to | `>=`     |
| smaller than or equal to | `<=`     |
|                          |          |
| containing               | `in`     |
| does not contain         | `not in` |
|                          |          |
| same as                  | `is`     |
| not same as              | `is not` |

Conditions may be combined using the keywords: `and`, `or`, `not`.

## Examples

```python
small = 1
big = 10
middle = 5

if small == 1:
    print('small = 1')    # will be printed

if small >= 2:
    print('small >= 2')   # will not be printed
else:
    print('small != 2')   # will be printed

if small < middle < big:  # notation of between
    print('middle is between small and big')

it_is_daytime_now = True
if it_is_daytime_now:
    print('The Sun shines now')
```
